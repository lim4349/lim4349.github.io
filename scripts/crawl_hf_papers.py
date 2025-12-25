#!/usr/bin/env python3
"""
Hugging Face Daily Papers 크롤링 스크립트
GitHub Actions에서 실행하여 일일 논문을 수집하고 Jekyll 포스트로 변환합니다.
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


class HFDailyPapersCrawler:
    """Hugging Face Daily Papers 크롤러"""

    def __init__(self, posts_dir: str = "_posts", data_dir: str = "_data/papers"):
        self.posts_dir = Path(posts_dir)
        self.posts_dir.mkdir(exist_ok=True)

        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.base_url = "https://huggingface.co"
        self.papers_url = "https://huggingface.co/papers"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def fetch_daily_papers(self, target_date: Optional[datetime] = None) -> List[Dict]:
        """특정 날짜의 논문 목록을 가져옵니다 (좋아요 수 포함)"""
        if target_date is None:
            target_date = datetime.utcnow()

        papers = self._fetch_daily_from_web(target_date)

        # 좋아요 수로 정렬 후 상위 10개 선택
        papers.sort(key=lambda x: x.get("likes", 0), reverse=True)
        top_papers = papers[:10]

        # 상위 10개의 상세 정보 가져오기
        enriched_papers = []
        for i, paper in enumerate(top_papers, 1):
            print(f"  [{i}/10] 수집 중: {paper.get('title', 'Unknown')[:50]}...")
            enriched = self._enrich_paper_details(paper)
            enriched_papers.append(enriched)
            time.sleep(1)

        enriched_papers.sort(key=lambda x: x.get("likes", 0), reverse=True)
        return enriched_papers

    def _fetch_daily_from_web(self, target_date: datetime) -> List[Dict]:
        """웹 페이지에서 일일 논문 목록 가져오기"""
        papers = []
        date_str = target_date.strftime("%Y-%m-%d")
        url = f"{self.papers_url}/date/{date_str}"

        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            paper_containers = soup.find_all(
                "div", class_=re.compile(r"flex\s+w-full\s+gap-6", re.I)
            )
            for container in paper_containers:
                try:
                    heading = container.find("h3")
                    if not heading:
                        continue

                    title_link = heading.find("a")
                    if not title_link:
                        continue

                    title = title_link.get_text(strip=True)
                    paper_url = title_link.get("href", "")
                    if not paper_url:
                        continue

                    if not paper_url.startswith("http"):
                        paper_url = (
                            self.base_url + paper_url
                            if paper_url.startswith("/")
                            else f"{self.base_url}/papers/{paper_url}"
                        )

                    # 좋아요 수 추출
                    likes = self._extract_likes_from_container(container)

                    # 기관 정보 추출
                    institution = self._extract_institution(container, heading)

                    papers.append(
                        {
                            "title": title,
                            "url": paper_url,
                            "published": target_date.isoformat(),
                            "likes": likes,
                            "institution": institution,
                        }
                    )
                except Exception:
                    continue
        except Exception:
            pass

        return papers

    def _extract_likes_from_container(self, container) -> int:
        """컨테이너에서 좋아요 수 추출"""
        for elem in container.find_all("div"):
            classes = elem.get("class", [])
            if isinstance(classes, list):
                classes_str = " ".join(classes)
            else:
                classes_str = str(classes)

            if "leading-none" in classes_str:
                text = elem.get_text(strip=True)
                if text.isdigit():
                    num = int(text)
                    if 1 <= num <= 100000:
                        return num
        return 0

    def _extract_institution(self, container, heading) -> str:
        """컨테이너에서 기관 정보 추출"""
        current = heading.next_sibling
        for _ in range(10):
            if not current:
                break
            if hasattr(current, "get_text"):
                text = current.get_text(strip=True)
                if text and 2 < len(text) < 200 and not re.match(r"^[\d\s\-]+$", text):
                    return text
            current = getattr(current, "next_sibling", None)
        return ""

    def _enrich_paper_details(self, paper: Dict) -> Dict:
        """논문 상세 페이지에서 추가 정보 가져오기"""
        url = paper.get("url", "")
        if not url:
            return paper

        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # 좋아요 수 업데이트
            likes = self._extract_likes_from_detail_page(soup)
            if likes > paper.get("likes", 0):
                paper["likes"] = likes

            # 제목
            if not paper.get("title"):
                h1 = soup.find("h1") or soup.find("title")
                if h1:
                    paper["title"] = h1.get_text(strip=True)

            # 논문 링크
            for link in soup.find_all("a", href=True):
                href = link.get("href", "")
                if re.search(r"arxiv\.org", href, re.I):
                    if not href.startswith("http"):
                        href = (
                            "https://arxiv.org" + href if href.startswith("/") else href
                        )
                    paper["paper_link"] = href
                    break
                elif re.search(r"\.pdf$", href, re.I) and not paper.get("paper_link"):
                    paper["paper_link"] = (
                        self.base_url + href if href.startswith("/") else href
                    )
                    break

            # 코드 링크
            for link in soup.find_all("a", href=re.compile(r"github", re.I)):
                paper["code_link"] = link.get("href", "")
                break

            # Abstract 추출
            if not paper.get("abstract") or len(paper.get("abstract", "")) < 50:
                paper["abstract"] = self._extract_abstract(
                    soup, paper.get("paper_link", "")
                )

        except Exception:
            pass

        return paper

    def _extract_likes_from_detail_page(self, soup) -> int:
        """상세 페이지에서 좋아요 수 추출"""
        for elem in soup.find_all("div"):
            classes = elem.get("class", [])
            if isinstance(classes, list):
                classes_str = " ".join(classes)
            else:
                classes_str = str(classes)

            if "leading-none" in classes_str:
                text = elem.get_text(strip=True)
                if text.isdigit():
                    num = int(text)
                    if 1 <= num <= 100000:
                        return num
        return 0

    def _extract_abstract(self, soup, paper_link: str) -> str:
        """Abstract 추출"""
        abstract = ""

        # 논문 링크에서 시도
        if paper_link:
            try:
                paper_response = requests.get(
                    paper_link, timeout=30, headers=self.headers
                )
                paper_response.raise_for_status()
                paper_soup = BeautifulSoup(paper_response.content, "html.parser")

                abstract_elem = (
                    paper_soup.find("blockquote", class_="abstract")
                    or paper_soup.find("div", class_="abstract")
                    or paper_soup.find("span", class_="abstract-text")
                    or paper_soup.find(class_=re.compile(r"abstract", re.I))
                )

                if abstract_elem:
                    abstract_text = abstract_elem.get_text(separator=" ", strip=True)
                    abstract_text = re.sub(
                        r"^Abstract\s*:?\s*", "", abstract_text, flags=re.I
                    )
                    abstract_text = re.sub(
                        r"^arXiv\s*:?\s*\d+\.\d+\s*", "", abstract_text, flags=re.I
                    )
                    if len(abstract_text) >= 50:
                        abstract = abstract_text.strip()
            except Exception:
                pass

        # Hugging Face 페이지에서 시도
        if not abstract or len(abstract) < 50:
            for selector in ['div[class*="abstract"]', 'div[class*="summary"]']:
                for elem in soup.select(selector):
                    text = elem.get_text(separator=" ", strip=True)
                    if 100 <= len(text) <= 2000:
                        if not any(
                            phrase in text.lower()
                            for phrase in [
                                "join the discussion",
                                "subscribe",
                                "get trending papers",
                            ]
                        ):
                            abstract = text
                            break

            # main/article에서 긴 문단 찾기
            if not abstract:
                for container in soup.find_all(["main", "article"]):
                    for p in container.find_all(["p", "div"], limit=10):
                        text = p.get_text(separator=" ", strip=True)
                        if 150 <= len(text) <= 2000 and len(text.split()) >= 20:
                            if not any(
                                phrase in text.lower()
                                for phrase in [
                                    "join the discussion",
                                    "subscribe",
                                    "get trending papers",
                                ]
                            ):
                                abstract = text
                                break
                    if abstract:
                        break

        return abstract

    def has_existing_post(self, target_date: datetime) -> bool:
        """특정 날짜의 포스트 파일이 이미 존재하는지 확인"""
        date_str = target_date.strftime("%Y-%m-%d")
        filename = f"{date_str}-daily-papers-summary.md"
        filepath = self.posts_dir / filename
        return filepath.exists()

    def save_daily_data(
        self, papers: List[Dict], target_date: Optional[datetime] = None
    ) -> Optional[str]:
        """일간 논문 데이터를 JSON으로 저장"""
        if not papers:
            return None

        if target_date is None:
            target_date = datetime.utcnow()

        date_str = target_date.strftime("%Y-%m-%d")
        filename = f"daily-{date_str}.json"
        filepath = self.data_dir / filename

        # 기존 파일 비교
        if filepath.exists():
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
                    existing_dict = {
                        (p.get("url", ""), p.get("likes", 0))
                        for p in existing_data.get("papers", [])
                    }
                    new_dict = {
                        (p.get("url", ""), p.get("likes", 0))
                        for p in papers
                        if p.get("url")
                    }

                    if existing_dict == new_dict:
                        print(f"데이터 동일: {filename} (저장 스킵)")
                        return None
            except Exception:
                pass

        data = {
            "date": date_str,
            "crawled_at": datetime.utcnow().isoformat(),
            "total_papers": len(papers),
            "papers": papers,
        }

        filepath.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"데이터 저장: {filename} ({len(papers)}개 논문)")
        return str(filepath)

    def generate_monthly_summary(self, year: int, month: int) -> Dict:
        """월간 요약 생성"""
        daily_data = []
        start_date = datetime(year, month, 1)
        end_date = (
            datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
        )

        for i in range((end_date - start_date).days):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime("%Y-%m-%d")
            daily_file = self.data_dir / f"daily-{date_str}.json"

            if daily_file.exists():
                try:
                    with open(daily_file, "r", encoding="utf-8") as f:
                        daily_data.append(json.load(f))
                except Exception:
                    pass

        # 중복 제거 및 정렬
        all_papers = []
        seen_urls = set()
        for daily in daily_data:
            for paper in daily.get("papers", []):
                url = paper.get("url", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_papers.append(paper)

        all_papers.sort(key=lambda x: x.get("likes", 0), reverse=True)
        top_papers = all_papers[:20]

        # 태그 통계
        tag_stats = defaultdict(int)
        for paper in all_papers:
            for tag in paper.get("tags", []):
                tag_stats[tag] += 1

        summary = {
            "year": year,
            "month": month,
            "generated_at": datetime.utcnow().isoformat(),
            "total_papers": len(all_papers),
            "total_likes": sum(p.get("likes", 0) for p in all_papers),
            "average_likes": round(
                sum(p.get("likes", 0) for p in all_papers) / len(all_papers), 2
            )
            if all_papers
            else 0,
            "days_crawled": len(daily_data),
            "top_papers": top_papers,
            "top_tags": [
                {"tag": tag, "count": count}
                for tag, count in sorted(
                    tag_stats.items(), key=lambda x: x[1], reverse=True
                )[:10]
            ],
        }

        if len(all_papers) == 0:
            return summary

        filename = f"monthly-{year}-{month:02d}.json"
        filepath = self.data_dir / filename

        # 기존 파일 비교
        if filepath.exists():
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
                    existing_urls = {
                        p.get("url", "") for p in existing_data.get("top_papers", [])
                    }
                    new_urls = {p.get("url", "") for p in top_papers if p.get("url")}

                    if existing_urls == new_urls:
                        print(f"월간 요약 동일: {filename} (저장 스킵)")
                        return summary
            except Exception:
                pass

        filepath.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"월간 요약 생성: {filename}")
        return summary

    def create_daily_summary_post(
        self,
        papers: List[Dict],
        target_date: Optional[datetime] = None,
        force_update: bool = False,
    ) -> Optional[str]:
        """일간 요약 포스트 생성"""
        if not papers:
            return None

        if target_date is None:
            target_date = datetime.utcnow()

        kst_date = target_date + timedelta(hours=9)
        post_date = kst_date.replace(hour=9, minute=15, second=0, microsecond=0)
        filename_date = target_date.strftime("%Y-%m-%d")
        filename = f"{filename_date}-daily-papers-summary.md"
        filepath = self.posts_dir / filename

        # 기존 파일 확인
        if filepath.exists() and not force_update:
            try:
                existing_content = filepath.read_text(encoding="utf-8")
                existing_urls = set(
                    re.findall(
                        r"https://huggingface\.co/papers/[^\s\)]+", existing_content
                    )
                )
                new_urls = {
                    paper.get("url", "") for paper in papers if paper.get("url")
                }

                if existing_urls == new_urls:
                    print(f"기존 포스트 동일: {filename} (업데이트 스킵)")
                    return None
            except Exception:
                pass

        # Front Matter
        front_matter = f"""---
title: Hugging Face Daily Papers - {filename_date}
date: {post_date.strftime("%Y-%m-%d %H:%M:%S")} +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

"""

        content = f"# Hugging Face Daily Papers - {filename_date}\n\n"
        content += (
            f"총 **{len(papers)}개**의 논문이 수집되었습니다.\n\n## 📊 좋아요 순위\n\n"
        )

        for i, paper in enumerate(papers, 1):
            content += f"{i}. **{paper.get('title', 'Untitled')}** - 👍 {paper.get('likes', 0)}\n"
            if paper.get("institution"):
                content += f"   - 기관: {paper['institution']}\n"
            content += f"   - [HF 페이지]({paper.get('url', '#')})\n"
            if paper.get("paper_link"):
                content += f"   - [논문 링크]({paper['paper_link']})\n"
            if paper.get("abstract"):
                content += f"   - Abstract: {paper['abstract']}\n"
            content += "\n"

        filepath.write_text(front_matter + content, encoding="utf-8")
        print(f"포스트 저장: {filename}")
        return str(filepath)

    def create_monthly_summary_post(
        self, summary: Dict, force_update: bool = False
    ) -> Optional[str]:
        """월간 요약 포스트 생성"""
        if summary["total_papers"] == 0:
            return None

        year, month = summary["year"], summary["month"]
        date_str = f"{year}-{month:02d}"
        filename = f"{date_str}-01-monthly-papers-summary.md"
        filepath = self.posts_dir / filename

        if filepath.exists() and not force_update:
            try:
                existing_content = filepath.read_text(encoding="utf-8")
                existing_urls = set(
                    re.findall(
                        r"https://huggingface\.co/papers/[^\s\)]+", existing_content
                    )
                )
                new_urls = {
                    paper.get("url", "")
                    for paper in summary["top_papers"]
                    if paper.get("url")
                }

                if existing_urls == new_urls:
                    print(f"기존 월간 포스트 동일: {filename} (업데이트 스킵)")
                    return None
            except Exception:
                pass

        front_matter = f"""---
title: Hugging Face Papers Monthly Summary - {year}년 {month}월
date: {year}-{month:02d}-01 09:00:00 +0900
categories: [Daily Papers, 월간]
tags: [huggingface, papers, monthly, ai, summary]
author: lim4349
---

"""

        content = (
            f"# Hugging Face Papers 월간 요약 - {year}년 {month}월\n\n## 📊 통계\n\n"
        )
        content += f"- **총 논문 수**: {summary['total_papers']}개\n"
        content += f"- **총 좋아요 수**: {summary['total_likes']:,}\n"
        content += f"- **평균 좋아요 수**: {summary['average_likes']:.2f}\n"
        content += f"- **수집 일수**: {summary['days_crawled']}일\n\n"
        content += "## 🔥 가장 인기 있는 논문 Top 20\n\n"

        for i, paper in enumerate(summary["top_papers"], 1):
            content += f"{i}. **{paper.get('title', 'Untitled')}** - 👍 {paper.get('likes', 0)}\n"
            if paper.get("institution"):
                content += f"   - 기관: {paper['institution']}\n"
            content += f"   - [HF 페이지]({paper.get('url', '#')})\n"
            if paper.get("paper_link"):
                content += f"   - [논문 링크]({paper['paper_link']})\n"
            if paper.get("abstract"):
                content += f"   - Abstract: {paper['abstract']}\n"
            content += "\n"

        if summary["top_tags"]:
            content += "## 🏷️ 인기 태그 Top 10\n\n"
            for i, tag_info in enumerate(summary["top_tags"], 1):
                content += f"{i}. `{tag_info['tag']}` - {tag_info['count']}회\n"
            content += "\n"

        filepath.write_text(front_matter + content, encoding="utf-8")
        print(f"월간 포스트 저장: {filename}")
        return str(filepath)


def main():
    """메인 함수"""
    print("=" * 50)
    print("Hugging Face Daily Papers 크롤링 시작")
    print("=" * 50)

    crawler = HFDailyPapersCrawler()

    now_utc = datetime.utcnow()
    now_kst = now_utc + timedelta(hours=9)
    target_date = now_utc

    print(
        f"\n현재 시간: UTC {now_utc.strftime('%Y-%m-%d %H:%M')}, KST {now_kst.strftime('%Y-%m-%d %H:%M')}"
    )
    print(f"크롤링 대상: {target_date.strftime('%Y-%m-%d')}")

    # 논문 크롤링
    papers = crawler.fetch_daily_papers(target_date)

    if not papers:
        print("논문을 찾지 못했습니다.")
        return

    print(f"\n총 {len(papers)}개 논문 수집 완료")

    # 데이터 저장 및 포스트 생성
    is_evening_crawl = 14 <= now_utc.hour < 15
    force_update = is_evening_crawl and crawler.has_existing_post(target_date)

    crawler.save_daily_data(papers, target_date)
    post_path = crawler.create_daily_summary_post(
        papers, target_date, force_update=force_update
    )

    if post_path:
        print(f"✅ 포스트 생성: {post_path}")

    # 월간 요약 (매월 1일 오전)
    if target_date.day == 1 and 2 <= now_utc.hour < 3:
        prev_month = target_date.replace(day=1) - timedelta(days=1)
        print(f"\n월간 요약 생성: {prev_month.year}년 {prev_month.month}월")
        summary = crawler.generate_monthly_summary(prev_month.year, prev_month.month)
        if summary["total_papers"] > 0:
            crawler.create_monthly_summary_post(summary)

    print("\n" + "=" * 50)
    print(f"크롤링 완료: {len(papers)}개 논문 처리")
    print("=" * 50)


if __name__ == "__main__":
    main()
