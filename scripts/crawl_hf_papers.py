#!/usr/bin/env python3
"""
Hugging Face Daily Papers 크롤링 스크립트
GitHub Actions에서 실행하여 일일 논문을 수집하고 Jekyll 포스트로 변환합니다.
일간 데이터를 JSON으로 저장하고, 좋아요 수로 정렬하며, Abstract도 수집합니다.
"""

import re
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
from collections import defaultdict
import time
try:
    import feedparser
except ImportError:
    feedparser = None


class HFDailyPapersCrawler:
    """Hugging Face Daily Papers 크롤러"""
    
    def __init__(self, posts_dir: str = "_posts", data_dir: str = "_data/papers"):
        self.posts_dir = Path(posts_dir)
        self.posts_dir.mkdir(exist_ok=True)
        
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Hugging Face Daily Papers 관련 URL들
        self.base_url = "https://huggingface.co"
        self.papers_url = "https://huggingface.co/papers"
        # 여러 RSS 피드 URL 시도
        self.rss_urls = [
            "https://huggingface.co/blog/tags/papers/rss.xml",
            "https://huggingface.co/blog/rss.xml",  # 전체 블로그 RSS
        ]
        self.rss_url = self.rss_urls[0]  # 기본값
    
    def fetch_daily_papers(self, target_date: Optional[datetime] = None) -> List[Dict]:
        """
        특정 날짜의 논문 목록을 가져옵니다 (좋아요 수 포함).
        
        Args:
            target_date: 크롤링할 날짜 (None이면 오늘)
            
        Returns:
            논문 정보 딕셔너리 리스트 (좋아요 수로 정렬됨)
        """
        if target_date is None:
            target_date = datetime.utcnow()
        
        papers = []
        
        # RSS 피드에서 논문 가져오기
        if feedparser:
            try:
                papers.extend(self._fetch_from_rss(target_date))
            except Exception:
                pass
        
        # 웹 페이지에서 논문 가져오기
        try:
            papers.extend(self._fetch_daily_from_web(target_date))
        except Exception:
            pass
        
        # 중복 제거 (URL 기준)
        seen_urls = set()
        unique_papers = []
        for paper in papers:
            url = paper.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_papers.append(paper)
        
        # 좋아요 수로 정렬 (내림차순)
        unique_papers.sort(key=lambda x: x.get('likes', 0), reverse=True)
        
        # 상위 10개만 선택
        top_papers = unique_papers[:10]
        print(f"\n[선택] 총 {len(unique_papers)}개 중 상위 10개 선택")
        
        # 상위 10개만 상세 정보 가져오기 (Abstract 포함)
        enriched_papers = []
        for i, paper in enumerate(top_papers, 1):
            try:
                print(f"  [{i}/10] 상세 정보 수집 중: {paper.get('title', 'Unknown')[:50]}...")
                enriched = self._enrich_paper_details(paper)
                enriched_papers.append(enriched)
                # 요청 간 딜레이 (서버 부하 방지)
                time.sleep(1)
            except Exception as e:
                print(f"  상세 정보 가져오기 실패 ({paper.get('url', 'unknown')}): {e}")
                enriched_papers.append(paper)
        
        # 최종 정렬 (좋아요 수로)
        enriched_papers.sort(key=lambda x: x.get('likes', 0), reverse=True)
        
        print(f"\n[완료] 최종 {len(enriched_papers)}개 논문 수집 완료")
        
        return enriched_papers
    
    def _fetch_from_rss(self, target_date: datetime) -> List[Dict]:
        """RSS 피드에서 특정 날짜의 논문 정보 가져오기"""
        if feedparser is None:
            return []
        
        papers = []
        feed = None
        
        # RSS URL 시도
        for rss_url in self.rss_urls:
            try:
                feed = feedparser.parse(rss_url)
                if feed.entries:
                    print(f"RSS 피드: {len(feed.entries)}개 항목")
                    break
            except Exception:
                continue
        
        if not feed or not feed.entries:
            return papers
        
        target_date_str = target_date.strftime('%Y-%m-%d')
        yesterday = (target_date - timedelta(days=1)).strftime('%Y-%m-%d')
        
        # 날짜 매칭
        for entry in feed.entries[:30]:
            entry_date = entry.get('published', '')
            if (target_date_str in entry_date or yesterday in entry_date or
                self._is_same_date(entry_date, target_date) or
                self._is_same_date(entry_date, target_date - timedelta(days=1))):
                papers.append({
                    'title': entry.get('title', ''),
                    'url': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'summary': entry.get('summary', ''),
                    'likes': 0
                })
        
        # 날짜 매칭 실패 시 최신 10개 사용
        if not papers:
            for entry in feed.entries[:10]:
                papers.append({
                    'title': entry.get('title', ''),
                    'url': entry.get('link', ''),
                    'published': entry.get('published', datetime.utcnow().isoformat()),
                    'summary': entry.get('summary', ''),
                    'likes': 0
                })
        
        return papers
    
    def check_date_has_papers(self, target_date: datetime) -> bool:
        """
        특정 날짜에 논문이 있는지 확인
        
        Args:
            target_date: 확인할 날짜
            
        Returns:
            논문이 있으면 True, 없으면 False
        """
        date_str = target_date.strftime('%Y-%m-%d')
        url = f"{self.papers_url}/date/{date_str}"
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 페이지의 날짜 제목 확인 (h1 또는 특정 클래스)
            # 페이지에 날짜가 표시되고 논문 항목이 있으면 True
            paper_headings = soup.find_all('h3')
            
            # 논문 제목이 있는지 확인 (최소 1개 이상)
            if paper_headings:
                # 실제로 논문 제목인지 확인 (너무 짧거나 특정 패턴이면 제외)
                valid_headings = [
                    h for h in paper_headings 
                    if h.find('a') and len(h.get_text(strip=True)) > 10
                ]
                if len(valid_headings) >= 1:
                    return True
            
            return False
        except Exception as e:
            print(f"날짜 확인 실패 ({url}): {e}")
            return False
    
    def _fetch_daily_from_web(self, target_date: datetime) -> List[Dict]:
        """웹 페이지에서 일일 논문 목록 가져오기"""
        papers = []
        
        # 올바른 URL 형식: https://huggingface.co/papers/date/YYYY-MM-DD
        # 실제 예시: https://huggingface.co/papers/date/2025-10-31
        date_str = target_date.strftime('%Y-%m-%d')
        url = f"{self.papers_url}/date/{date_str}"
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 논문 항목 찾기 (h3 태그로 제목 찾기)
            # 구조: h3 > a (제목 링크), 좋아요 수는 같은 레벨에 있음
            paper_headings = soup.find_all('h3')
            
            
            for heading in paper_headings:
                try:
                    # 제목 링크 찾기
                    title_link = heading.find('a')
                    if not title_link:
                        continue
                    
                    title = title_link.get_text(strip=True)
                    if not title:
                        continue
                    
                    paper_url = title_link.get('href', '')
                    
                    if not paper_url.startswith('http'):
                        if paper_url.startswith('/'):
                            paper_url = self.base_url + paper_url
                        else:
                            paper_url = f"{self.base_url}/papers/{paper_url}"
                    
                    # 좋아요 수 찾기 - h3의 부모 요소에서 찾기
                    likes = 0
                    parent = heading.parent
                    if parent:
                        # 부모 요소의 텍스트에서 숫자 찾기
                        parent_text = parent.get_text()
                        # 좋아요 수는 보통 큰 숫자이고, h3 근처에 있음
                        # 형식: "97\n" 또는 " 97 " 같은 패턴
                        numbers = re.findall(r'\b(\d+)\b', parent_text)
                        
                        # h3 다음에 나오는 숫자가 좋아요 수일 가능성이 높음
                        # 또는 h3 앞에 있는 큰 숫자
                        if numbers:
                            # 첫 번째 큰 숫자 (10 이상)를 좋아요 수로 추정
                            for num_str in numbers:
                                try:
                                    num = int(num_str)
                                    if num >= 10:  # 좋아요는 보통 10 이상
                                        likes = num
                                        break
                                except (ValueError, TypeError):
                                    pass
                        
                        # h3의 다음 형제 요소 확인
                        if likes == 0:
                            current = heading.next_sibling
                            checked = 0
                            while current and checked < 3:
                                if hasattr(current, 'get_text'):
                                    text = current.get_text(strip=True)
                                    like_match = re.search(r'^(\d+)$', text)
                                    if like_match:
                                        num = int(like_match.group(1))
                                        if num >= 10:
                                            likes = num
                                            break
                                current = getattr(current, 'next_sibling', None)
                                checked += 1
                    
                    # 기관 정보 추출 - h3 다음에 오는 텍스트에서 찾기
                    institution = ''
                    if parent:
                        # h3 다음에 오는 모든 형제 요소 확인
                        current = heading.next_sibling
                        checked = 0
                        while current and checked < 10:
                            if hasattr(current, 'get_text'):
                                text = current.get_text(strip=True)
                                # 기관명은 보통 텍스트이고, 링크나 특정 구조를 가짐
                                # "ByteDance-Seed ByteDance Seed" 같은 패턴
                                if text and len(text) > 2 and len(text) < 200:
                                    # 숫자나 특수 문자만 있는 것은 제외
                                    if not re.match(r'^[\d\s\-]+$', text):
                                        # 링크나 텍스트 노드에서 추출
                                        if hasattr(current, 'find'):
                                            # 링크 안의 텍스트 추출
                                            link = current.find('a')
                                            if link:
                                                link_text = link.get_text(strip=True)
                                                if link_text and len(link_text) > 2:
                                                    institution = link_text
                                                    break
                                            else:
                                                # 일반 텍스트 노드
                                                institution = text
                                                break
                                        else:
                                            institution = text
                                            break
                            current = getattr(current, 'next_sibling', None)
                            checked += 1
                        
                        # 부모 요소에서 기관 관련 링크나 텍스트 찾기
                        if not institution:
                            # a 태그 중 href에 특정 패턴이 있는 것 찾기 (org, company 등)
                            for link in parent.find_all('a', href=True):
                                href = link.get('href', '')
                                link_text = link.get_text(strip=True)
                                # 기관 페이지 링크 패턴이나 텍스트가 있는 경우
                                if (link_text and len(link_text) > 2 and len(link_text) < 200 and
                                    ('/org/' in href or '/company/' in href or 
                                     not href.startswith('/papers/') and not href.startswith('#'))):
                                    institution = link_text
                                    break
                            
                            # 부모 요소의 전체 텍스트에서 기관명 패턴 찾기
                            if not institution:
                                parent_text = parent.get_text(separator=' ', strip=True)
                                # 제목과 좋아요 수 사이의 텍스트에서 기관명 찾기
                                lines = parent_text.split('\n')
                                for line in lines:
                                    line = line.strip()
                                    # 제목이 아닌 긴 텍스트 라인 찾기
                                    if (line and len(line) > 3 and len(line) < 200 and 
                                        title.lower() not in line.lower() and
                                        not re.match(r'^[\d\s]+$', line)):
                                        # 링크나 특수 문자가 아닌 일반 텍스트인 경우
                                        if not line.startswith('http') and not line.startswith('/'):
                                            institution = line
                                            break
                    
                    if title and paper_url:
                        papers.append({
                            'title': title,
                            'url': paper_url,
                            'published': target_date.isoformat(),
                            'likes': likes,
                            'institution': institution
                        })
                except Exception:
                    continue
                    
        except Exception:
            pass
        
        return papers
    
    def _enrich_paper_details(self, paper: Dict) -> Dict:
        """논문 상세 페이지에서 추가 정보 가져오기 (Abstract 포함)"""
        url = paper.get('url', '')
        if not url:
            return paper
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 좋아요 수, 논문 링크, 코드 링크, 태그 추출
            likes = paper.get('likes', 0)
            for elem in soup.find_all(['span', 'div', 'button'], class_=re.compile(r'like|favorite', re.I)):
                match = re.search(r'(\d+)', elem.get_text(strip=True))
                if match:
                    likes = max(likes, int(match.group(1)))
            
            title = paper.get('title', '')
            if not title:
                h1 = soup.find('h1') or soup.find('title')
                if h1:
                    title = h1.get_text(strip=True)
            
            paper_link = paper.get('paper_link', '')
            # arXiv, PDF, DOI 링크 찾기
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                # arXiv 링크 (abs/, pdf/, e-print 등)
                if re.search(r'arxiv\.org|arxiv\.org/abs/|arxiv\.org/pdf/', href, re.I):
                    paper_link = href
                    if not paper_link.startswith('http'):
                        # 상대 경로 처리
                        if href.startswith('/abs/') or href.startswith('/pdf/'):
                            paper_link = 'https://arxiv.org' + href
                        elif href.startswith('/'):
                            paper_link = 'https://arxiv.org/abs/' + href.lstrip('/')
                    break
                # PDF 링크
                elif re.search(r'\.pdf$', href, re.I) and not paper_link:
                    paper_link = href
                    if not paper_link.startswith('http'):
                        paper_link = self.base_url + paper_link if paper_link.startswith('/') else href
                # DOI 링크
                elif re.search(r'doi\.org|doi:', href, re.I) and not paper_link:
                    paper_link = href
                    if not paper_link.startswith('http'):
                        paper_link = 'https://doi.org' + href if href.startswith('/') else href
            
            code_link = paper.get('code_link', '')
            for link in soup.find_all('a', href=re.compile(r'(github|gitlab)', re.I)):
                code_link = link.get('href', '')
                break
            
            tags = paper.get('tags', [])
            if not tags:
                tags = [tag.get_text(strip=True) for tag in soup.find_all(['a', 'span'], class_=re.compile(r'tag', re.I))[:10]]
            
            # 기관 정보는 목록 페이지에서만 추출 (상세 페이지에서는 찾지 않음)
            institution = paper.get('institution', '')
            
            # Abstract 추출: 논문 링크(paper_link)에서 먼저 시도
            abstract = paper.get('abstract', '')
            
            # 1. 논문 링크(arXiv 등)에서 Abstract 추출 시도
            if paper_link:
                try:
                    paper_response = requests.get(paper_link, timeout=30, headers=headers)
                    paper_response.raise_for_status()
                    paper_soup = BeautifulSoup(paper_response.content, 'html.parser')
                    
                    # arXiv 페이지의 Abstract 추출
                    # arXiv는 보통 <blockquote class="abstract"> 또는 <div class="abstract"> 사용
                    abstract_elem = None
                    
                    # arXiv 형식 1: blockquote.abstract
                    abstract_elem = paper_soup.find('blockquote', class_='abstract')
                    if not abstract_elem:
                        # arXiv 형식 2: div.abstract
                        abstract_elem = paper_soup.find('div', class_='abstract')
                    if not abstract_elem:
                        # arXiv 형식 3: span.abstract-text
                        abstract_elem = paper_soup.find('span', class_='abstract-text')
                    if not abstract_elem:
                        # arXiv 형식 4: class에 abstract 포함
                        abstract_elem = paper_soup.find(class_=re.compile(r'abstract', re.I))
                    
                    if abstract_elem:
                        abstract_text = abstract_elem.get_text(separator=' ', strip=True)
                        # "Abstract:" 같은 레이블 제거
                        abstract_text = re.sub(r'^Abstract\s*:?\s*', '', abstract_text, flags=re.I)
                        # "arXiv:" 같은 접두사 제거
                        abstract_text = re.sub(r'^arXiv\s*:?\s*\d+\.\d+\s*', '', abstract_text, flags=re.I)
                        if len(abstract_text) >= 50:
                            abstract = abstract_text.strip()
                            print(f"    ✅ 논문 페이지에서 Abstract 추출 성공 ({len(abstract)}자)")
                except Exception as e:
                    print(f"    ⚠️ 논문 페이지 접근 실패 ({paper_link}): {e}")
            
            # 2. 논문 링크에서 추출 실패 시 Hugging Face 페이지에서 시도
            if not abstract or len(abstract) < 50:
                abstract_candidates = []
                
                # 명시적인 abstract/summary 섹션 찾기
                for selector in [
                    'div[class*="abstract"]',
                    'div[class*="summary"]',
                    'section[class*="abstract"]',
                    'section[class*="summary"]',
                    'p[class*="abstract"]',
                    'p[class*="summary"]',
                ]:
                    for elem in soup.select(selector):
                        text = elem.get_text(separator=' ', strip=True)
                        if text and 100 <= len(text) <= 2000:
                            abstract_candidates.append(text)
                
                # main/article에서 첫 번째 긴 문단 찾기
                for container in soup.find_all(['main', 'article']):
                    paragraphs = container.find_all(['p', 'div'], limit=10)
                    for p in paragraphs:
                        text = p.get_text(separator=' ', strip=True)
                        if (text and 150 <= len(text) <= 2000 and
                            'Join the discussion' not in text and
                            'Subscribe' not in text and
                            'Get trending papers' not in text and
                            'on this paper page' not in text and
                            not text.startswith('http') and
                            len(text.split()) >= 20):
                            abstract_candidates.append(text)
                            break
                
                # 가장 적합한 후보 선택
                if abstract_candidates:
                    filtered = []
                    unwanted_phrases = [
                        'Join the discussion',
                        'on this paper page',
                        'Subscribe',
                        'Get trending papers',
                        'View on',
                        'Download',
                        'Like',
                        'Share',
                    ]
                    
                    for candidate in abstract_candidates:
                        has_unwanted = any(phrase.lower() in candidate.lower() for phrase in unwanted_phrases)
                        if not has_unwanted and len(candidate) >= 100:
                            filtered.append(candidate)
                    
                    if filtered:
                        abstract = max(filtered, key=len)
                    elif abstract_candidates:
                        abstract = max(abstract_candidates, key=len)
                        for unwanted in unwanted_phrases:
                            if unwanted.lower() in abstract.lower():
                                parts = re.split(re.escape(unwanted), abstract, flags=re.I)
                                if parts:
                                    abstract = parts[0].strip()
                                    break
                
                # 메타 태그 시도 (마지막 수단)
                if not abstract or len(abstract) < 50:
                    for meta in soup.find_all('meta', attrs={'name': ['description'], 'property': ['og:description']}):
                        desc = meta.get('content', '').strip()
                        if (desc and len(desc) >= 100 and
                            'Join the discussion' not in desc and
                            'on this paper page' not in desc):
                            abstract = desc
                            break
            
            # 3. 최종 정리
            if abstract:
                # 불필요한 구문 제거
                unwanted_patterns = [
                    r'Join the discussion.*?$',
                    r'on this paper page.*?$',
                    r'Subscribe.*?$',
                    r'Get trending papers.*?$',
                ]
                for pattern in unwanted_patterns:
                    abstract = re.sub(pattern, '', abstract, flags=re.I).strip()
                
                # 너무 짧거나 불필요한 텍스트 제거
                if (len(abstract) < 50 or
                    abstract.lower() in ['join the discussion', 'subscribe', 'get trending papers'] or
                    'on this paper page' in abstract.lower()):
                    abstract = ''
            
            
            # 업데이트된 정보 반환
            paper.update({
                'title': title,
                'abstract': abstract,
                'likes': likes,
                'paper_link': paper_link,
                'code_link': code_link,
                'tags': tags,
                'institution': institution,
                'description': abstract[:500] if abstract else ''  # 요약
            })
            
        except Exception:
            pass
        
        return paper
    
    def _is_same_date(self, date_str: str, target_date: datetime) -> bool:
        """날짜 문자열이 target_date와 같은 날인지 확인"""
        try:
            # 다양한 날짜 형식 파싱
            for fmt in ['%a, %d %b %Y %H:%M:%S %z', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d']:
                try:
                    parsed = datetime.strptime(date_str[:19], fmt)
                    return parsed.date() == target_date.date()
                except (ValueError, TypeError):
                    continue
        except (ValueError, TypeError):
            pass
        return False
    
    def is_weekend(self, target_date: datetime) -> bool:
        """
        특정 날짜가 주말(토요일, 일요일)인지 확인
        
        Args:
            target_date: 확인할 날짜
            
        Returns:
            주말이면 True, 평일이면 False
        """
        # weekday(): 월요일=0, 일요일=6
        # 토요일=5, 일요일=6이면 주말
        return target_date.weekday() >= 5
    
    def has_existing_post(self, target_date: datetime) -> bool:
        """
        특정 날짜의 포스트 파일이 이미 존재하는지 확인
        
        Args:
            target_date: 확인할 날짜
            
        Returns:
            파일이 있으면 True, 없으면 False
        """
        date_str = target_date.strftime('%Y-%m-%d')
        filename = f"{date_str}-daily-papers-summary.md"
        filepath = self.posts_dir / filename
        return filepath.exists()
    
    def save_daily_data(self, papers: List[Dict], target_date: Optional[datetime] = None) -> Optional[str]:
        """
        일간 논문 데이터를 JSON으로 저장
        
        Returns:
            저장된 파일 경로 또는 None (논문이 없으면 None)
        """
        # 논문이 없으면 저장하지 않음
        if not papers:
            print("⚠️ 논문이 0개입니다. 데이터를 저장하지 않습니다.")
            return None
        
        if target_date is None:
            target_date = datetime.utcnow()
        
        date_str = target_date.strftime('%Y-%m-%d')
        filename = f"daily-{date_str}.json"
        filepath = self.data_dir / filename
        
        # 기존 파일이 있으면 내용 비교
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_urls = {p.get('url', '') for p in existing_data.get('papers', [])}
                    new_urls = {p.get('url', '') for p in papers if p.get('url')}
                    
                    # 내용이 같으면 저장하지 않음
                    if existing_urls == new_urls:
                        print(f"기존 데이터와 동일: {filename} (저장 스킵)")
                        return None
            except Exception:
                pass
        
        data = {
            'date': date_str,
            'crawled_at': datetime.utcnow().isoformat(),
            'total_papers': len(papers),
            'papers': papers
        }
        
        filepath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"일간 데이터 저장: {filename} ({len(papers)}개 논문)")
        
        return str(filepath)
    
    def generate_monthly_summary(self, year: int, month: int) -> Dict:
        """
        월간 요약 생성
        
        Args:
            year: 연도
            month: 월 (1-12)
            
        Returns:
            월간 요약 데이터
        """
        # 해당 월의 모든 일간 데이터 로드
        daily_data = []
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
        
        current_date = start_date
        while current_date < end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            daily_file = self.data_dir / f"daily-{date_str}.json"
            
            if daily_file.exists():
                try:
                    with open(daily_file, 'r', encoding='utf-8') as f:
                        daily = json.load(f)
                        daily_data.append(daily)
                except Exception as e:
                    print(f"일간 데이터 로드 실패 ({date_str}): {e}")
            
            current_date += timedelta(days=1)
        
        # 모든 논문 수집
        all_papers = []
        paper_ids = set()
        
        for daily in daily_data:
            for paper in daily.get('papers', []):
                paper_id = paper.get('url', '') or paper.get('title', '')
                if paper_id and paper_id not in paper_ids:
                    paper_ids.add(paper_id)
                    all_papers.append(paper)
        
        # 좋아요 수로 정렬
        all_papers.sort(key=lambda x: x.get('likes', 0), reverse=True)
        
        # 통계
        total_papers = len(all_papers)
        total_likes = sum(p.get('likes', 0) for p in all_papers)
        top_papers = all_papers[:20]  # Top 20
        
        # 태그별 통계
        tag_stats = defaultdict(int)
        for paper in all_papers:
            for tag in paper.get('tags', []):
                tag_stats[tag] += 1
        
        top_tags = sorted(tag_stats.items(), key=lambda x: x[1], reverse=True)[:10]
        
        summary = {
            'year': year,
            'month': month,
            'generated_at': datetime.utcnow().isoformat(),
            'total_papers': total_papers,
            'total_likes': total_likes,
            'average_likes': round(total_likes / total_papers, 2) if total_papers > 0 else 0,
            'days_crawled': len(daily_data),
            'top_papers': top_papers,
            'top_tags': [{'tag': tag, 'count': count} for tag, count in top_tags],
            'daily_summaries': [
                {
                    'date': d.get('date'),
                    'total_papers': d.get('total_papers', 0)
                }
                for d in daily_data
            ]
        }
        
        # 논문이 없으면 JSON 저장하지 않음
        if total_papers == 0:
            print("⚠️ 월간 요약에 논문이 0개입니다. JSON을 저장하지 않습니다.")
            return summary
        
        # 월간 요약 저장 (논문이 있을 때만)
        filename = f"monthly-{year}-{month:02d}.json"
        filepath = self.data_dir / filename
        
        # 기존 파일이 있으면 내용 비교
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_urls = {p.get('url', '') for p in existing_data.get('top_papers', [])}
                    new_urls = {p.get('url', '') for p in top_papers if p.get('url')}
                    
                    # 내용이 같으면 저장하지 않음
                    if existing_urls == new_urls:
                        print(f"기존 월간 요약 데이터와 동일: {filename} (저장 스킵)")
                        return summary
            except Exception:
                pass
        
        filepath.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"월간 요약 생성: {filename}")
        return summary
    
    def create_daily_summary_post(self, papers: List[Dict], target_date: Optional[datetime] = None, force_update: bool = True) -> Optional[str]:
        """
        일간 요약 포스트 생성
        
        Args:
            papers: 논문 리스트
            target_date: 대상 날짜
            force_update: 기존 파일이 있어도 업데이트할지 여부
        
        Returns:
            저장된 파일 경로 또는 None
        """
        # 논문이 없으면 포스트 생성하지 않음
        if not papers:
            print("⚠️ 논문이 0개입니다. 포스트를 생성하지 않습니다.")
            return None
        
        if target_date is None:
            target_date = datetime.utcnow()
        
        # 한국 시간 기준으로 날짜 설정
        kst_date = target_date + timedelta(hours=9)
        post_date = kst_date.replace(hour=9, minute=15, second=0, microsecond=0)
        
        # 파일명 생성
        filename_date = target_date.strftime('%Y-%m-%d')
        filename = f"{filename_date}-daily-papers-summary.md"
        filepath = self.posts_dir / filename
        
        # force_update가 True면 무조건 덮어쓰기 (좋아요 수 업데이트용)
        if force_update and filepath.exists():
            print(f"기존 파일 강제 업데이트: {filename} (좋아요 수 등 업데이트)")
        elif filepath.exists():
            # 기존 파일이 있고 force_update가 False일 때만 내용 비교하여 스킵 여부 결정
            try:
                existing_content = filepath.read_text(encoding='utf-8')
                # 기존 파일에서 논문 URL 추출
                existing_urls = set(re.findall(r'https://huggingface\.co/papers/[^\s\)]+', existing_content))
                # 새로 크롤링한 논문 URL 목록
                new_urls = {paper.get('url', '') for paper in papers if paper.get('url')}
                
                # Abstract도 비교하여 변경사항 확인
                existing_has_bad_abstract = 'Abstract: Join the discussion on this paper page' in existing_content
                new_has_good_abstract = any(
                    paper.get('abstract', '') and 
                    len(paper.get('abstract', '')) > 50 and
                    'Join the discussion' not in paper.get('abstract', '') and
                    'on this paper page' not in paper.get('abstract', '')
                    for paper in papers
                )
                
                # URL이 같고 Abstract가 개선되지 않았으면 업데이트하지 않음
                if existing_urls == new_urls and not new_has_good_abstract:
                    print(f"이미 존재하는 일간 요약: {filename} (내용 동일, 업데이트 스킵)")
                    return None
                
                # Abstract 개선이 있으면 업데이트
                if existing_urls == new_urls and existing_has_bad_abstract and new_has_good_abstract:
                    print(f"기존 파일 Abstract 개선 필요: {filename} (업데이트)")
                elif existing_urls != new_urls:
                    print(f"기존 파일 내용과 다름: {filename} (업데이트)")
            except Exception as e:
                print(f"기존 파일 확인 오류: {e}, 새로 생성합니다.")
        
        # 기존 파일이 없으면 새로 생성
        if not filepath.exists():
            print(f"새 파일 생성: {filename}")
        
        # Front Matter
        front_matter = {
            'title': f'Hugging Face Daily Papers - {filename_date}',
            'date': f"{post_date.strftime('%Y-%m-%d %H:%M:%S')} +0900",
            'categories': ['Daily Papers', '일간'],
            'tags': ['huggingface', 'papers', 'daily', 'ai'],
            'author': 'lim4349'
        }
        
        # 본문 생성
        content = f"# Hugging Face Daily Papers - {filename_date}\n\n"
        content += f"총 **{len(papers)}개**의 논문이 수집되었습니다.\n\n## 📊 좋아요 순위\n\n"
        
        for i, paper in enumerate(papers, 1):
            content += f"{i}. **{paper.get('title', 'Untitled')}** - 👍 {paper.get('likes', 0)}\n"
            if paper.get('institution'):
                content += f"   - 기관: {paper['institution']}\n"
            content += f"   - [HF 페이지]({paper.get('url', '#')})\n"
            if paper.get('paper_link'):
                content += f"   - [논문 링크]({paper['paper_link']})\n"
            if paper.get('abstract'):
                content += f"   - Abstract: {paper['abstract']}\n"
            content += "\n"
        
        # Front Matter + Content
        yaml_header = "---\n"
        for key, value in front_matter.items():
            yaml_header += f"{key}: {value}\n" if not isinstance(value, list) else f"{key}: {value}\n"
        yaml_header += "---\n\n"
        full_content = yaml_header + content
        
        filepath.write_text(full_content, encoding='utf-8')
        print(f"일간 요약 포스트 저장: {filename}")
        
        return str(filepath)
    
    def create_monthly_summary_post(self, summary: Dict, force_update: bool = False) -> Optional[str]:
        """
        월간 요약 포스트 생성
        
        Args:
            summary: 월간 요약 데이터
            force_update: 기존 파일이 있어도 업데이트할지 여부 (기본값: False)
        
        Returns:
            저장된 파일 경로 또는 None
        """
        # 논문이 없으면 포스트 생성하지 않음
        if summary['total_papers'] == 0:
            print("⚠️ 월간 요약에 논문이 0개입니다. 포스트를 생성하지 않습니다.")
            return None
        
        year = summary['year']
        month = summary['month']
        date_str = f"{year}-{month:02d}"
        
        filename = f"{date_str}-01-monthly-papers-summary.md"
        filepath = self.posts_dir / filename
        
        # 기존 파일이 있으면 내용 비교
        if filepath.exists():
            try:
                existing_content = filepath.read_text(encoding='utf-8')
                # 기존 파일에서 논문 URL 추출
                existing_urls = set(re.findall(r'https://huggingface\.co/papers/[^\s\)]+', existing_content))
                # 새로 생성할 논문 URL 목록
                new_urls = {paper.get('url', '') for paper in summary['top_papers'] if paper.get('url')}
                
                # 내용이 같으면 업데이트하지 않음
                if existing_urls == new_urls and not force_update:
                    print(f"이미 존재하는 월간 요약: {filename} (내용 동일, 업데이트 스킵)")
                    return None
                
                if existing_urls == new_urls and force_update:
                    print(f"기존 파일 내용과 동일: {filename} (업데이트 스킵)")
                    return None
                
                print(f"기존 파일 내용과 다름: {filename} (업데이트)")
            except Exception as e:
                print(f"기존 파일 확인 오류: {e}, 새로 생성합니다.")
        
        if not filepath.exists():
            print(f"새 월간 요약 생성: {filename}")
        
        # Front Matter
        front_matter = {
            'title': f'Hugging Face Papers Monthly Summary - {year}년 {month}월',
            'date': f"{year}-{month:02d}-01 09:00:00 +0900",
            'categories': ['Daily Papers', '월간'],
            'tags': ['huggingface', 'papers', 'monthly', 'ai', 'summary'],
            'author': 'lim4349'
        }
        
        # 본문 생성
        content = f"# Hugging Face Papers 월간 요약 - {year}년 {month}월\n\n## 📊 통계\n\n"
        content += f"- **총 논문 수**: {summary['total_papers']}개\n"
        content += f"- **총 좋아요 수**: {summary['total_likes']:,}\n"
        content += f"- **평균 좋아요 수**: {summary['average_likes']:.2f}\n"
        content += f"- **수집 일수**: {summary['days_crawled']}일\n\n"
        content += "## 🔥 가장 인기 있는 논문 Top 20\n\n"
        
        if summary['top_papers']:
            for i, paper in enumerate(summary['top_papers'], 1):
                content += f"{i}. **{paper.get('title', 'Untitled')}** - 👍 {paper.get('likes', 0)}\n"
                if paper.get('institution'):
                    content += f"   - 기관: {paper['institution']}\n"
                content += f"   - [HF 페이지]({paper.get('url', '#')})\n"
                if paper.get('paper_link'):
                    content += f"   - [논문 링크]({paper['paper_link']})\n"
                if paper.get('abstract'):
                    content += f"   - Abstract: {paper['abstract']}\n"
                content += "\n"
        else:
            content += "이번 달에 수집된 논문이 없습니다.\n\n"
        
        if summary['top_tags']:
            content += "## 🏷️ 인기 태그 Top 10\n\n"
            for i, tag_info in enumerate(summary['top_tags'], 1):
                content += f"{i}. `{tag_info['tag']}` - {tag_info['count']}회\n"
            content += "\n"
        
        # Front Matter + Content
        yaml_header = "---\n"
        for key, value in front_matter.items():
            yaml_header += f"{key}: {value}\n" if not isinstance(value, list) else f"{key}: {value}\n"
        yaml_header += "---\n\n"
        full_content = yaml_header + content
        
        filepath.write_text(full_content, encoding='utf-8')
        print(f"월간 요약 포스트 저장: {filename}")
        
        return str(filepath)


def main():
    """메인 함수"""
    print("=" * 50)
    print("Hugging Face Daily Papers 크롤링 시작")
    print("=" * 50)
    
    crawler = HFDailyPapersCrawler()
    
    # 오늘 날짜로 크롤링 (UTC 기준)
    now_utc = datetime.utcnow()
    now_kst = now_utc + timedelta(hours=9)
    target_date = now_utc
    
    print(f"\n현재 시간: UTC {now_utc.strftime('%Y-%m-%d %H:%M')}, KST {now_kst.strftime('%Y-%m-%d %H:%M')}")
    print(f"크롤링 대상 날짜: {target_date.strftime('%Y-%m-%d')}")
    
    # 0단계: 주말 체크
    is_weekend = crawler.is_weekend(target_date)
    if is_weekend:
        weekday_name = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'][target_date.weekday()]
        print(f"\n⚠️ 오늘은 {weekday_name}(주말)입니다.")
        print("   Hugging Face는 주말에 새로운 논문을 업로드하지 않을 수 있습니다.")
        print("   크롤링을 스킵합니다.")
        print("\n" + "=" * 50)
        print("크롤링 완료: 주말 스킵")
        print("=" * 50)
        return
    
    # 1단계: 크롤링 시간대 확인
    is_morning_crawl = 1 <= now_utc.hour < 12  # UTC 01:00-12:00 (KST 10:00-21:00)
    is_evening_crawl = 13 <= now_utc.hour < 14  # UTC 13:00-14:00 (KST 22:00-23:00)
    
    # 2단계: 오늘 날짜 페이지에 논문이 있는지 확인
    print(f"\n[1단계] 오늘 날짜 페이지 확인 중: {target_date.strftime('%Y-%m-%d')}")
    has_papers = crawler.check_date_has_papers(target_date)
    
    # 3단계: 기존 포스트 파일 확인 (오후 크롤링 시)
    existing_post = crawler.has_existing_post(target_date) if is_evening_crawl else False
    
    if not has_papers:
        if is_morning_crawl:
            print(f"⚠️ 오늘 날짜 ({target_date.strftime('%Y-%m-%d')})에 논문이 없습니다.")
            print("   페이지가 아직 갱신되지 않았을 수 있습니다.")
            print("   크롤링을 중단합니다. 오후 10시에 다시 확인합니다.")
            print("\n" + "=" * 50)
            print("크롤링 완료: 논문 없음 (스킵)")
            print("=" * 50)
            return
        else:
            # 오후 크롤링인데도 논문이 없고, 기존 포스트도 없으면 완전 스킵
            if not existing_post:
                print(f"⚠️ 오늘 날짜 ({target_date.strftime('%Y-%m-%d')})에 논문이 없습니다.")
                print("   오전에도 크롤링되지 않았고, 논문도 없습니다.")
                print("   크롤링을 중단합니다.")
                print("\n" + "=" * 50)
                print("크롤링 완료: 논문 없음 (스킵)")
                print("=" * 50)
                return
            else:
                # 오후 크롤링: 기존 포스트는 있지만 현재 논문이 없는 경우
                # (좋아요 수 업데이트는 불가능하므로 스킵)
                print(f"⚠️ 오늘 날짜 ({target_date.strftime('%Y-%m-%d')})에 논문이 없습니다.")
                print("   기존 포스트가 있지만 현재 논문이 없어 업데이트할 내용이 없습니다.")
                print("   크롤링을 중단합니다.")
                print("\n" + "=" * 50)
                print("크롤링 완료: 업데이트할 내용 없음 (스킵)")
                print("=" * 50)
                return
    
    print("✅ 오늘 날짜에 논문이 있습니다. 크롤링을 시작합니다.")
    
    # 3단계: 논문 크롤링
    papers = crawler.fetch_daily_papers(target_date)
    
    print(f"\n총 {len(papers)}개의 논문을 찾았습니다.\n")
    
    # 논문이 없으면 종료
    if not papers:
        print("⚠️ 논문이 0개입니다. 크롤링을 중단합니다.")
        print("\n" + "=" * 50)
        print("크롤링 완료: 0개의 논문을 처리했습니다.")
        print("=" * 50)
        return
    
    # 논문이 있으면 출력
    print("좋아요 순위 (Top 10):")
    for i, paper in enumerate(papers[:10], 1):
        likes = paper.get('likes', 0)
        title = paper.get('title', 'Unknown')[:60]
        print(f"  {i}. 👍 {likes} - {title}")
    
    # 4단계: 크롤링 시간대에 따라 업데이트 방식 결정
    # 오전 크롤링(UTC 01:00, KST 10:00): 새 파일 생성 (기존 파일과 비교하여 변경사항이 있을 때만 업데이트)
    # 오후 크롤링(UTC 13:00, KST 22:00): 기존 파일이 있으면 좋아요 수 업데이트를 위해 덮어쓰기
    if is_evening_crawl:
        if existing_post:
            print("\n[오후 크롤링] 기존 포스트 파일이 존재합니다.")
            print("   좋아요 수 업데이트를 위해 파일을 덮어쓰기합니다.")
            force_update = True
        else:
            print("\n[오후 크롤링] 기존 포스트 파일이 없습니다.")
            print("   오전 크롤링이 스킵되었지만 페이지가 갱신되어 새로 생성합니다.")
            # 기존 파일이 없으면 일반 생성 모드 (내용 비교 후 생성)
            force_update = False
    else:
        print("\n[오전 크롤링] 새 논문 크롤링 및 파일 생성/업데이트합니다.")
        force_update = False
    
    # 논문이 있을 때만 데이터 저장 및 포스트 생성
    crawler.save_daily_data(papers, target_date)
    post_path = crawler.create_daily_summary_post(papers, target_date, force_update=force_update)
    if post_path:
        if force_update:
            print(f"✅ 일간 요약 포스트 업데이트 (좋아요 수 반영): {post_path}")
        else:
            print(f"✅ 일간 요약 포스트 생성/업데이트: {post_path}")
    else:
        print("ℹ️ 일간 요약 포스트 업데이트 없음")
    
    # 월간 요약 생성 (이전 달) - 매월 1일에만 실행
    # 오늘이 매월 1일이면 이전 달의 월간 요약 생성
    is_first_of_month = target_date.day == 1
    
    if is_first_of_month and is_morning_crawl:
        try:
            # 이전 달 계산
            if target_date.month == 1:
                # 1월이면 작년 12월
                prev_year = target_date.year - 1
                prev_month = 12
            else:
                prev_year = target_date.year
                prev_month = target_date.month - 1
            
            print(f"\n[월간 요약] 이전 달({prev_year}년 {prev_month}월) 월간 요약 생성 중...")
            summary = crawler.generate_monthly_summary(prev_year, prev_month)
            # 월간 요약은 논문이 있을 때만 생성
            if summary['total_papers'] > 0:
                monthly_post_path = crawler.create_monthly_summary_post(summary, force_update=False)
                if monthly_post_path:
                    print(f"✅ 월간 요약 포스트 생성/업데이트: {monthly_post_path}")
                else:
                    print("ℹ️ 월간 요약 포스트 업데이트 없음 (내용 동일 또는 이미 존재)")
            else:
                print(f"⚠️ {prev_year}년 {prev_month}월에 수집된 논문이 없습니다.")
        except Exception as e:
            print(f"⚠️ 월간 요약 생성 실패: {e}")
    elif is_first_of_month:
        print(f"\n[월간 요약] 오늘은 {target_date.day}일이지만 오후 크롤링이므로 월간 요약을 생성하지 않습니다.")
    else:
        print(f"\n[월간 요약] 오늘은 {target_date.day}일이므로 월간 요약을 생성하지 않습니다. (매월 1일에만 생성)")
    
    print("\n" + "=" * 50)
    print(f"크롤링 완료: {len(papers)}개의 논문을 처리했습니다.")
    print("=" * 50)


if __name__ == "__main__":
    main()
