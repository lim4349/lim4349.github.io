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
        
        try:
            # RSS 피드에서 오늘 날짜의 논문 가져오기
            if feedparser is not None:
                rss_papers = self._fetch_from_rss(target_date)
                papers.extend(rss_papers)
                print(f"RSS 피드에서 {len(rss_papers)}개 논문 발견")
            else:
                print("⚠️ feedparser가 설치되지 않았습니다. RSS 피드를 사용할 수 없습니다.")
        except Exception as e:
            print(f"RSS 피드 가져오기 실패: {e}")
            import traceback
            traceback.print_exc()
        
        # 웹 페이지에서도 시도
        try:
            web_papers = self._fetch_daily_from_web(target_date)
            papers.extend(web_papers)
            print(f"웹 스크래핑에서 {len(web_papers)}개 논문 발견")
        except Exception as e:
            print(f"웹 스크래핑 실패: {e}")
            import traceback
            traceback.print_exc()
        
        # 각 논문의 상세 정보 가져오기 (Abstract 포함)
        enriched_papers = []
        for paper in papers:
            try:
                enriched = self._enrich_paper_details(paper)
                enriched_papers.append(enriched)
                # 요청 간 딜레이 (서버 부하 방지)
                time.sleep(1)
            except Exception as e:
                print(f"상세 정보 가져오기 실패 ({paper.get('url', 'unknown')}): {e}")
                enriched_papers.append(paper)
        
        # 중복 제거 (URL 기준)
        seen_urls = set()
        unique_papers = []
        for paper in enriched_papers:
            url = paper.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_papers.append(paper)
        
        # 좋아요 수로 정렬 (내림차순)
        unique_papers.sort(key=lambda x: x.get('likes', 0), reverse=True)
        
        return unique_papers
    
    def _fetch_from_rss(self, target_date: datetime) -> List[Dict]:
        """RSS 피드에서 특정 날짜의 논문 정보 가져오기"""
        if feedparser is None:
            return []
        
        papers = []
        feed = None
        
        # 여러 RSS URL 시도
        for rss_url in self.rss_urls:
            try:
                print(f"RSS 피드 가져오기 시도: {rss_url}")
                feed = feedparser.parse(rss_url)
                
                if not feed.entries:
                    print(f"⚠️ RSS 피드에 항목이 없습니다: {rss_url}")
                    print(f"   피드 상태: {feed.get('status', 'unknown')}")
                    continue
                
                print(f"✅ RSS 피드에서 총 {len(feed.entries)}개 항목 발견: {rss_url}")
                break  # 성공한 RSS 피드 사용
                
            except Exception as e:
                print(f"⚠️ RSS 피드 실패 ({rss_url}): {e}")
                continue
        
        # feed가 없으면 반환
        if not feed or not feed.entries:
            print("⚠️ 사용 가능한 RSS 피드가 없습니다.")
            return papers
        
        target_date_str = target_date.strftime('%Y-%m-%d')
        yesterday = (target_date - timedelta(days=1)).strftime('%Y-%m-%d')
        
        # 최신 항목들 확인 (날짜 매칭이 실패해도 최신 항목 사용)
        checked_count = 0
        for entry in feed.entries[:30]:  # 최신 30개 확인
            checked_count += 1
            entry_date_str = entry.get('published', '')
            
            # 날짜 매칭 (오늘 또는 어제)
            if (target_date_str in entry_date_str or 
                yesterday in entry_date_str or 
                self._is_same_date(entry_date_str, target_date) or
                self._is_same_date(entry_date_str, target_date - timedelta(days=1))):
                paper = {
                    'title': entry.get('title', ''),
                    'url': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'summary': entry.get('summary', ''),
                    'likes': 0  # RSS에서는 좋아요 수를 가져올 수 없음
                }
                papers.append(paper)
                print(f"  - 매칭된 논문: {paper['title'][:50]}...")
        
        # 날짜 매칭이 실패했으면 최신 10개 사용
        if not papers and checked_count > 0:
            print("⚠️ 날짜 매칭 실패, 최신 항목 사용")
            for entry in feed.entries[:10]:
                paper = {
                    'title': entry.get('title', ''),
                    'url': entry.get('link', ''),
                    'published': entry.get('published', datetime.utcnow().isoformat()),
                    'summary': entry.get('summary', ''),
                    'likes': 0
                }
                papers.append(paper)
        
        return papers
    
    def _fetch_daily_from_web(self, target_date: datetime) -> List[Dict]:
        """웹 페이지에서 일일 논문 목록 가져오기"""
        papers = []
        
        # 올바른 URL 형식: /papers/date/YYYY-MM-DD
        date_str = target_date.strftime('%Y-%m-%d')
        url = f"{self.papers_url}/date/{date_str}"
        
        print(f"웹 페이지 크롤링 시도: {url}")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 논문 항목 찾기 (h3 태그로 제목 찾기)
            # 구조: h3 > a (제목 링크), 좋아요 수는 같은 레벨에 있음
            paper_headings = soup.find_all('h3')
            
            if not paper_headings:
                print("⚠️ h3 태그를 찾을 수 없습니다. 페이지 구조 확인 필요")
                # 대안: 모든 링크에서 papers 링크 찾기
                all_links = soup.find_all('a', href=re.compile(r'/papers/[^/]+$'))
                print(f"  대안: {len(all_links)}개 papers 링크 발견")
            
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
                    
                    if title and paper_url:
                        papers.append({
                            'title': title,
                            'url': paper_url,
                            'published': target_date.isoformat(),
                            'likes': likes
                        })
                        print(f"  - 발견: {title[:50]}... (👍 {likes})")
                        
                except Exception as e:
                    print(f"  논문 파싱 오류: {e}")
                    continue
            
            print(f"웹 페이지에서 {len(papers)}개 논문 발견")
                    
        except Exception as e:
            print(f"웹 페이지 크롤링 실패: {e}")
            import traceback
            traceback.print_exc()
        
        return papers
    
    def _enrich_paper_details(self, paper: Dict) -> Dict:
        """논문 상세 페이지에서 추가 정보 가져오기 (Abstract 포함)"""
        url = paper.get('url', '')
        if not url:
            return paper
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Abstract/Description 추출
            abstract = paper.get('abstract', '')
            
            # 다양한 패턴으로 Abstract 찾기
            abstract_selectors = [
                ('div', {'class': re.compile(r'abstract|description|summary', re.I)}),
                ('p', {'class': re.compile(r'abstract|description|summary', re.I)}),
                ('section', {'class': re.compile(r'abstract|description|summary', re.I)}),
            ]
            
            for tag, attrs in abstract_selectors:
                elem = soup.find(tag, attrs)
                if elem:
                    abstract = elem.get_text(strip=True)
                    if abstract:
                        break
            
            # 메타 설명도 시도
            if not abstract:
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if meta_desc:
                    abstract = meta_desc.get('content', '')
            
            # 좋아요 수 추출 (상세 페이지에서)
            likes = paper.get('likes', 0)
            like_elements = soup.find_all(['span', 'div', 'button'], class_=re.compile(r'like|favorite|star', re.I))
            for elem in like_elements:
                like_text = elem.get_text(strip=True)
                like_match = re.search(r'(\d+)', like_text)
                if like_match:
                    likes = max(likes, int(like_match.group(1)))
            
            # 제목 업데이트
            title = paper.get('title', '')
            if not title:
                title_elem = soup.find('h1') or soup.find('title')
                if title_elem:
                    title = title_elem.get_text(strip=True)
            
            # 논문 링크 (arXiv, PDF 등)
            paper_link = paper.get('paper_link', '')
            paper_links = soup.find_all('a', href=re.compile(r'(arxiv|pdf|doi)', re.I))
            if paper_links and not paper_link:
                paper_link = paper_links[0].get('href', '')
            
            # 코드 링크
            code_link = paper.get('code_link', '')
            code_links = soup.find_all('a', href=re.compile(r'(github|gitlab)', re.I))
            if code_links and not code_link:
                code_link = code_links[0].get('href', '')
            
            # 태그
            tags = paper.get('tags', [])
            tag_elements = soup.find_all(['a', 'span'], class_=re.compile(r'tag|label|badge', re.I))
            if not tags:
                tags = [tag.get_text(strip=True) for tag in tag_elements[:10]]
            
            # 업데이트된 정보 반환
            paper.update({
                'title': title,
                'abstract': abstract,
                'likes': likes,
                'paper_link': paper_link,
                'code_link': code_link,
                'tags': tags,
                'description': abstract[:500] if abstract else ''  # 요약
            })
            
        except Exception as e:
            print(f"상세 정보 추출 실패 ({url}): {e}")
        
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
    
    def save_daily_data(self, papers: List[Dict], target_date: Optional[datetime] = None) -> str:
        """
        일간 논문 데이터를 JSON으로 저장
        
        Returns:
            저장된 파일 경로
        """
        if target_date is None:
            target_date = datetime.utcnow()
        
        date_str = target_date.strftime('%Y-%m-%d')
        filename = f"daily-{date_str}.json"
        filepath = self.data_dir / filename
        
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
        top_papers = all_papers[:10]  # Top 10
        
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
        
        # 월간 요약 저장
        filename = f"monthly-{year}-{month:02d}.json"
        filepath = self.data_dir / filename
        filepath.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
        
        print(f"월간 요약 생성: {filename}")
        return summary
    
    def create_daily_summary_post(self, papers: List[Dict], target_date: Optional[datetime] = None) -> Optional[str]:
        """
        일간 요약 포스트 생성
        
        Returns:
            저장된 파일 경로 또는 None
        """
        if target_date is None:
            target_date = datetime.utcnow()
        
        # 파일명 생성
        filename_date = target_date.strftime('%Y-%m-%d')
        filename = f"{filename_date}-daily-papers-summary.md"
        filepath = self.posts_dir / filename
        
        # 이미 존재하는 파일인지 확인
        if filepath.exists():
            print(f"이미 존재하는 일간 요약: {filename}")
            return None
        
        # Front Matter
        front_matter = {
            'title': f'Hugging Face Daily Papers - {filename_date}',
            'date': f"{target_date.strftime('%Y-%m-%d %H:%M:%S')} +0900",
            'categories': ['Daily Papers', '일간'],
            'tags': ['huggingface', 'papers', 'daily', 'ai'],
            'author': 'lim4349'
        }
        
        # 본문 생성
        content = f"# Hugging Face Daily Papers - {filename_date}\n\n"
        content += f"총 **{len(papers)}개**의 논문이 수집되었습니다.\n\n"
        
        # 좋아요 수별로 정렬된 목록
        content += "## 📊 좋아요 순위\n\n"
        
        for i, paper in enumerate(papers[:20], 1):  # Top 20
            likes = paper.get('likes', 0)
            title = paper.get('title', 'Untitled')
            url = paper.get('url', '#')
            
            content += f"{i}. **{title}** - 👍 {likes}\n"
            content += f"   - [HF 페이지]({url})\n"
            
            if paper.get('paper_link'):
                content += f"   - [논문 링크]({paper['paper_link']})\n"
            
            if paper.get('abstract'):
                abstract = paper['abstract'][:200] + "..." if len(paper['abstract']) > 200 else paper['abstract']
                content += f"   - Abstract: {abstract}\n"
            
            content += "\n"
        
        # Front Matter + Content 조합
        yaml_header = "---\n"
        for key, value in front_matter.items():
            if isinstance(value, list):
                yaml_header += f"{key}: {value}\n"
            else:
                yaml_header += f"{key}: {value}\n"
        yaml_header += "---\n\n"
        
        full_content = yaml_header + content
        
        filepath.write_text(full_content, encoding='utf-8')
        print(f"일간 요약 포스트 저장: {filename}")
        
        return str(filepath)
    
    def create_monthly_summary_post(self, summary: Dict) -> Optional[str]:
        """
        월간 요약 포스트 생성
        
        Returns:
            저장된 파일 경로 또는 None
        """
        year = summary['year']
        month = summary['month']
        date_str = f"{year}-{month:02d}"
        
        filename = f"{date_str}-01-monthly-papers-summary.md"
        filepath = self.posts_dir / filename
        
        if filepath.exists():
            print(f"이미 존재하는 월간 요약: {filename}")
            return None
        
        # Front Matter
        front_matter = {
            'title': f'Hugging Face Papers Monthly Summary - {year}년 {month}월',
            'date': f"{year}-{month:02d}-01 09:00:00 +0900",
            'categories': ['Daily Papers', '월간'],
            'tags': ['huggingface', 'papers', 'monthly', 'ai', 'summary'],
            'author': 'lim4349'
        }
        
        # 본문 생성
        content = f"# Hugging Face Papers 월간 요약 - {year}년 {month}월\n\n"
        content += "## 📊 통계\n\n"
        content += f"- **총 논문 수**: {summary['total_papers']}개\n"
        content += f"- **총 좋아요 수**: {summary['total_likes']:,}\n"
        content += f"- **평균 좋아요 수**: {summary['average_likes']:.2f}\n"
        content += f"- **수집 일수**: {summary['days_crawled']}일\n\n"
        
        # Top Papers
        content += "## 🔥 가장 인기 있는 논문 Top 10\n\n"
        for i, paper in enumerate(summary['top_papers'], 1):
            likes = paper.get('likes', 0)
            title = paper.get('title', 'Untitled')
            url = paper.get('url', '#')
            
            content += f"{i}. **{title}** - 👍 {likes}\n"
            content += f"   - [HF 페이지]({url})\n\n"
        
        # Top Tags
        if summary['top_tags']:
            content += "## 🏷️ 인기 태그 Top 10\n\n"
            for i, tag_info in enumerate(summary['top_tags'], 1):
                content += f"{i}. `{tag_info['tag']}` - {tag_info['count']}회\n"
            content += "\n"
        
        # YAML Header
        yaml_header = "---\n"
        for key, value in front_matter.items():
            if isinstance(value, list):
                yaml_header += f"{key}: {value}\n"
            else:
                yaml_header += f"{key}: {value}\n"
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
    
    # 오늘 날짜의 논문 가져오기
    target_date = datetime.utcnow()
    print(f"\n크롤링 대상 날짜: {target_date.strftime('%Y-%m-%d')}")
    
    papers = crawler.fetch_daily_papers(target_date)
    
    print(f"\n총 {len(papers)}개의 논문을 찾았습니다.\n")
    
    if papers:
        # 좋아요 수로 정렬된 목록 출력
        print("좋아요 순위 (Top 10):")
        for i, paper in enumerate(papers[:10], 1):
            likes = paper.get('likes', 0)
            title = paper.get('title', 'Unknown')[:60]
            print(f"  {i}. 👍 {likes} - {title}")
        
        # 일간 데이터 저장
        crawler.save_daily_data(papers, target_date)
        
        # 일간 요약 포스트 생성
        crawler.create_daily_summary_post(papers, target_date)
        
        # 월간 요약 생성 (이번 달)
        # 매일 월간 요약을 다시 생성하여 최신 데이터 반영
        # (매월 1일에만 생성하려면 아래 주석 해제)
        current_year = target_date.year
        current_month = target_date.month
        
        # 매월 1일에만 월간 요약 생성하려면 아래 주석 해제
        # if target_date.day == 1:
        summary = crawler.generate_monthly_summary(current_year, current_month)
        crawler.create_monthly_summary_post(summary)
    
    print("\n" + "=" * 50)
    print(f"크롤링 완료: {len(papers)}개의 논문을 처리했습니다.")
    print("=" * 50)


if __name__ == "__main__":
    main()
