# Hugging Face Daily Papers 자동 크롤링 설정 가이드

이 프로젝트는 GitHub Actions를 사용하여 Hugging Face Daily Papers를 자동으로 크롤링하고 Jekyll 블로그에 포스트로 추가하는 시스템입니다.

## 📋 전체 구조

```
lim4349.github.io/
├── .github/
│   └── workflows/
│       └── crawl-papers.yml      # GitHub Actions 워크플로우
├── scripts/
│   ├── crawl_hf_papers.py        # 크롤링 스크립트
│   └── README.md                 # 스크립트 설명서
├── _posts/                       # 생성된 Jekyll 포스트 저장 위치
├── requirements.txt              # Python 의존성
└── CRAWL_SETUP.md               # 이 파일
```

## 🚀 작동 방식

### 1. **자동 실행 스케줄**
- **매일 한국시간 오전 9시** (UTC 00:00) 자동 실행
- GitHub Actions에서 `schedule` 이벤트로 트리거

### 2. **크롤링 프로세스**
```
GitHub Actions 트리거
    ↓
Python 환경 설정
    ↓
의존성 설치 (requests, beautifulsoup4, feedparser)
    ↓
크롤링 스크립트 실행
    ↓
Hugging Face RSS/웹에서 최신 논문 수집
    ↓
논문 정보를 Jekyll 포스트 형식으로 변환
    ↓
_posts/ 디렉토리에 저장 (YYYY-MM-DD-title.md)
    ↓
변경사항 자동 커밋 & 푸시
    ↓
GitHub Pages 자동 빌드 & 배포
```

### 3. **데이터 소스**
- **주요**: Hugging Face Papers RSS 피드 (`https://huggingface.co/blog/tags/papers/rss.xml`)
- **백업**: 웹 스크래핑 (`https://huggingface.co/papers`)

## 🔧 설정 방법

### 1. **GitHub Actions 권한 설정**

Repository → Settings → Actions → General → Workflow permissions
- ✅ Read and write permissions 선택
- ✅ Allow GitHub Actions to create and approve pull requests (선택사항)

### 2. **스케줄 조정** (선택사항)

`.github/workflows/crawl-papers.yml` 파일에서 cron 스케줄 수정:

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 00:00 = KST 09:00
  # 예: 매일 UTC 12:00 = KST 21:00
  # - cron: '0 12 * * *'
```

### 3. **크롤링 개수 조정**

`scripts/crawl_hf_papers.py`의 `main()` 함수에서:

```python
papers = crawler.fetch_latest_papers(limit=5)  # 원하는 개수로 변경
```

### 4. **포스트 형식 커스터마이징**

`scripts/crawl_hf_papers.py`의 `create_jekyll_post()` 메서드를 수정하여 원하는 포맷으로 변경할 수 있습니다.

## 📝 생성되는 포스트 형식

각 논문은 다음과 같은 형식의 Markdown 파일로 생성됩니다:

```markdown
---
title: 논문 제목
date: 2024-01-01 09:00:00 +0900
categories: [Daily Papers, AI/ML]
tags: [paper, ai, huggingface, ...]
author: lim4349
---

## 📄 논문 제목

논문 설명 또는 요약...

### 🔗 Links

- **Hugging Face**: [원본 링크]
- **Paper**: [arXiv/PDF 링크] (있는 경우)
- **Code**: [GitHub 링크] (있는 경우)

### 🏷️ Tags

`tag1`, `tag2`, `tag3`...

---

*원본: [원본 링크]*
```

## 🧪 로컬 테스트

GitHub Actions 없이 로컬에서 테스트하려면:

```bash
# 의존성 설치
pip install -r requirements.txt

# 스크립트 실행
python scripts/crawl_hf_papers.py
```

생성된 포스트는 `_posts/` 디렉토리에서 확인할 수 있습니다.

## 🔍 문제 해결

### 크롤링이 작동하지 않는 경우

1. **GitHub Actions 로그 확인**
   - Repository → Actions 탭에서 워크플로우 실행 로그 확인
   - 에러 메시지 확인

2. **RSS 피드 확인**
   - `https://huggingface.co/blog/tags/papers/rss.xml` 접속하여 RSS 피드가 정상인지 확인

3. **권한 확인**
   - Repository Settings → Actions → Workflow permissions 확인

### 포스트가 생성되지 않는 경우

1. **중복 확인**: 이미 존재하는 포스트는 건너뜁니다
2. **날짜 형식**: 논문 발행 날짜가 올바르게 파싱되지 않을 수 있습니다
3. **제목 변환**: 특수 문자가 많은 제목은 파일명 변환 과정에서 문제가 될 수 있습니다

## 📊 모니터링

- **GitHub Actions**: Repository → Actions에서 워크플로우 실행 상태 확인
- **커밋 히스토리**: 자동 커밋 메시지로 크롤링 상태 추적 가능
- **포스트 확인**: `_posts/` 디렉토리에서 생성된 포스트 확인

## 🎯 향후 개선 가능 사항

1. **필터링 기능**: 특정 주제나 키워드만 크롤링
2. **중복 감지 개선**: URL 외에도 제목 유사도로 중복 판단
3. **요약 생성**: AI를 활용한 논문 요약 자동 생성
4. **카테고리 자동 분류**: 논문 내용 기반 카테고리 자동 지정
5. **이미지 다운로드**: 논문 썸네일 자동 다운로드

## 📚 참고 자료

- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [Jekyll 포스트 가이드](https://jekyllrb.com/docs/posts/)
- [Hugging Face Papers](https://huggingface.co/papers)
- [RSS 피드 형식](https://en.wikipedia.org/wiki/RSS)

---

**작성일**: 2024년
**버전**: 1.0.0



