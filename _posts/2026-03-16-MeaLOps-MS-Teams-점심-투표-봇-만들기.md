---
title: MeaLOps - MS Teams 점심 투표 봇 만들기
date: 2026-03-16 14:00:00 +0900
categories: ['개발']
tags: ['ms-teams', 'bot', 'typescript', 'ollama', 'llm', 'sqlite', 'nodejs']
author: lim4349
---

# MeaLOps - MS Teams 점심 투표 봇 만들기

매일 점심 메뉴를 정하는 고민을 해결하기 위해 MS Teams에서 동작하는 점심 투표 봇을 만들었다. 로컬 LLM(Ollama)을 활용한 AI 추천, 날씨 기반 메뉴 추천, 동점 처리 로직 등을 포함한 실용적인 프로젝트다.

## 기술 스택

| 레이어 | 기술 | 버전 |
|--------|------|------|
| **언어** | Node.js + TypeScript | 25.x |
| **프레임워크** | Express + MS Bot Framework | 5.x / 4.23 |
| **DB** | SQLite (better-sqlite3) | 12.x |
| **LLM** | Ollama (gemma3:12b) | 로컬 |
| **인증** | SingleTenant (CloudAdapter) | - |
| **스케줄링** | node-cron + setInterval | - |

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| **🗳️ 투표** | 다중 선택, 혼밥, 아무거나 / 토글 취소 / 사용자별 선택 상태 표시 |
| **🤖 AI 추천** | Ollama 기반, 블랙리스트·최근방문·날씨 반영, 새로고침 지원 |
| **⭐ 리뷰** | 방문일 기준 저장, 날짜별 독립 평점, 덮어쓰기 가능 |
| **📊 히스토리** | 주간/월간 조회, 리뷰 완료 여부 표시 |
| **📋 식당목록** | 이름/거리/가격/⭐점수 다중 정렬, 카테고리 그룹핑 |
| **🚫 블랙리스트** | 개인별 싫어하는 식당 제외 |
| **🏆 내 최애** | 자주 간 식당 TOP5 + 높은 평점 TOP5 |
| **🛵 배달 모드** | 배달 가능 식당만 필터링 |
| **⏰ 강제 결정** | 11:30 자동 결정 (on/off) |

---

## 하루의 흐름

```
11:00  ──▶  투표 알림 카드 발송
           │
           │  사용자들이 식당 선택 (토글)
           │  혼밥 / 아무거나 선택 가능
           │
11:30  ──▶  강제 결정 (설정 시)
           │
           │  동점 처리:
           │  1. 최근 30일 방문 적은 곳
           │  2. 평균 평점 높은 곳
           │  3. 랜덤
           │
12:50  ──▶  리뷰 요청 카드 발송
```

---

## AI 추천 시스템

Ollama(gemma3:12b)를 활용해 날씨와 상황에 맞는 식당을 추천한다.

### 프롬프트 구성

```typescript
const prompt = `날씨: ${temp}도 ${description}. ${weatherInstruction}.
식당 목록: ${restaurantList}
제외(최근3일): ${recentVisits}
제외(블랙리스트): ${blacklisted}

위 식당 목록에서만 5개 추천. 각각 다른 카테고리면 더 좋음. JSON만 출력:
[{"name":"식당이름","reason":"날씨/음식 특성 위주로 짧게"},...]`;
```

### 날씨별 추천 전략

| 날씨 | 추천 전략 |
|------|----------|
| 비/눈 | 거리 가깝고 실내 편한 식당 우선 |
| < 10°C | 따뜻한 한식/국물류 우선 |
| > 25°C | 시원한 냉면/국수류/음료 우선 |
| 기타 | 평점 높은 식당 추천 |

### Fallback

Ollama 연결 실패 시, 날씨 기반 단순 로직으로 랜덤 5개를 추천한다.

---

## 동점 처리 로직

투표 결과가 동점일 때의 처리 순서다.

```
1. 최근 30일 방문 가장 적은 식당 우선
   └─ 동점이면 ↓
2. 평균 평점 높은 곳 우선
   └─ 동점이면 ↓
3. 랜덤 선택
```

```typescript
// Tie-breaker 1: 최근 방문 적은 곳
const dates = this.historyRepo.getRecentVisitDates(restaurant.id, 30);
const lastVisit = dates[0] ?? ''; // 가장 최근 방문일

// Tie-breaker 2: 평점 높은 곳
const avgRating = this.reviewRepo.getAverageRating(restaurant.id);

// Tie-breaker 3: 랜덤
const winner = candidates[Math.floor(Math.random() * candidates.length)];
```

---

## 스케줄러 구현

UTC 기반 서버에서 KST(+9시간)로 동작하도록 구현했다.

```typescript
setInterval(async () => {
  const now = new Date();
  const kstTime = new Date(now.getTime() + 9 * 60 * 60 * 1000);
  const hour = String(kstTime.getHours()).padStart(2, '0');
  const minute = String(kstTime.getMinutes()).padStart(2, '0');
  const hm = `${hour}:${minute}`;

  // 평일만 실행
  if (kstTime.getDay() >= 1 && kstTime.getDay() <= 5) {
    if (hm === '11:00') await this.sendVoteReminder();
    if (hm === '11:30') await this.makeForceDecision();
    if (hm === '12:50') await this.sendReviewReminder();
  }
}, 1000);
```

한국 공휴일도 하드코딩으로 처리했다 (2024-2026년).

---

## 개발 배경

원래 경영지원팀에서 매일 점심 메뉴를 정해줬는데, 이게 생각보다 스트레스가 많이 받는 일이었다. 수고를 덜어드리고자 이번에 제작하게 됐다. 진작 만들었으면 더 좋았을 듯.

---

## 개발하면서 겪은 문제들

### 1. Azure Portal 등록과 요금 함정

MS Teams 봇을 만들려면 Azure Portal에서 계정 연동하고 앱 등록을 해야 한다. "무료"라고 되어 있어서 회사 계정으로 등록했는데, 웬걸 한 달에 $4가 청구됐다.

알고 보니 **기본이 유료 요금제**고, 내부에서 별도로 "무료 요금제"를 신청해야만 무료다. 다행히 무료 크레딧이 있어서 퉁쳐질 듯. 추후 계속 모니터링 중.

### 2. 터널링 서비스 선택

회사 로컬 컴퓨터에서 서빙 중인데, Azure Portal과 연결하려면 공개 도메인이 필요했다.

| 서비스 | 장점 | 단점 |
|--------|------|------|
| **localtunnel** | 계정 불필요, subdomain 지정 가능 | 연결 불안정, 새로고침마다 서브도메인 변경 버그 |
| **ngrok** | 안정적, 무료 도메인 1개 제공 | 유료 도메인은 과금 |

처음엔 ngrok 계정 만들기가 귀찮아서 localtunnel을 썼는데, 연결이 너무 불안정해서 결국 ngrok으로 갈아탔다. 다행히 개발용 도메인 하나는 무료로 제공해서 현재 서빙 중.

### 3. Azure 생태계

강제로 Azure 생태계를 약간 맛보게 됐는데, **상대적으로 비주류인 이유를 알 수 있었다**. 너무 복잡하고 요구하는 게 많다. 그나마 다행인 건 Ollama와 SQLite는 로컬에서 돌아가니 Azure 리소스를 추가로 쓸 일은 없다는 점.

---

## 참고 자료

- [GitHub - MeaLOps](https://github.com/lim4349/mealops)
- [MS Bot Framework 문서](https://learn.microsoft.com/en-us/azure/bot-service/)
- [Ollama](https://ollama.ai/)

---

## 총평

**좋았던 점**:
- 실제 회사에서 매일 사용하는 실용적인 도구다
- 로컬 LLM(Ollama)을 활용해 API 비용 없이 AI 추천 기능을 구현했다
- Clean Architecture로 유지보수가 쉬운 구조다
- 동점 처리, 날씨 반영 등 디테일한 요구사항을 모두 구현했다

**아쉬웠던 점**:
- Ollama가 로컬에서 돌아가므로 서버 리소스를 많이 사용한다
- gemma3:12b 모델이 가끔 이상한 JSON을 반환할 때가 있다
- 공휴일 처리가 하드코딩이라 매년 업데이트가 필요하다

**결론**: 사내에서 매일 점심 메뉴를 정하는 실질적인 문제를 해결한 프로젝트다. LLM을 API 비용 없이 활용할 수 있어서 비용 효율적이다.

---

## FAQ

- **Ollama가 뭔가요?**
  - 로컬에서 LLM을 실행할 수 있는 오픈소스 도구입니다. API 비용 없이 gemma, llama 등의 모델을 사용할 수 있습니다.

- **왜 SQLite를 썼나요?**
  - 데이터 규모가 작고(식당 수십 개, 투표 기록), 단일 서버에서만 접근하므로 SQLite로 충분합니다. 별도 DB 서버 없이 파일 하나로 관리할 수 있어 편리합니다.

- **CloudAdapter와 BotFrameworkAdapter의 차이는?**
  - `CloudAdapter`는 v4.14+에서 도입된 새 어댑터로, `MicrosoftAppType`을 통한 명시적 테넌트 설정을 지원합니다. Single-Tenant 봇은 CloudAdapter를 사용해야 합니다.

- **동점 처리는 왜 이렇게 복잡한가요?**
  - 실제 사용 중 동표가 자주 발생했고, "왜 이 집이냐?"는 질문에 논리적인 근거가 필요했습니다. 최근 방문 → 평점 → 랜덤 순서로 공정성을 확보했습니다.
