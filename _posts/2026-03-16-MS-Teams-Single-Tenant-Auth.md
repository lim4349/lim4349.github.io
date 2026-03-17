---
title: MS Teams 봇 Single-Tenant 인증 문제 해결기
date: 2026-03-16 09:15:00 +0900
categories: ['정리']
tags: ['ms-teams', 'bot', 'azure', 'nodejs', 'typescript']
author: lim4349
---

# MS Teams 봇 Single-Tenant 인증 문제 해결기

MS Teams 봇 개발 중 카드 버튼은 동작하는데 텍스트 메시지 응답만 401 에러가 발생하는 문제를 해결한 과정이다.

## 증상

- **카드 버튼 클릭** → 정상 동작 ✅
- **텍스트 메시지 전송** → 응답 없음 ❌

```
[Activity] type=message name=- text="/밥줘" from=임성근
[onMessage] sendActivity FAILED: Authorization has been denied for this request.
[onMessage] error statusCode: 401
```

## 원인 분석

### 카드 버튼은 되는데 텍스트는 안 되는 이유

| 활동 타입 | 응답 방법 | 인증 필요 여부 |
|----------|----------|--------------|
| `invoke` (카드 액션) | HTTP 응답으로 직접 반환 | ❌ 불필요 |
| `message` (텍스트) | Bot Connector Service API 호출 | ✅ 필요 |

텍스트 메시지 응답은 Bot Connector Service에 HTTP 요청을 보내야 하므로 Bearer 토큰 인증이 필요하다.

### serviceUrl의 차이

수신된 활동의 `serviceUrl`을 확인해보면:

```
# 한국 리전 Single-Tenant
https://smba.trafficmanager.net/kr/2718d412-f6c4-4245-bb9f-5175b01e27d5/

# 일반 Multi-Tenant
https://smba.trafficmanager.net/amer/
```

Single-Tenant 봇은 URL에 테넌트 ID가 포함되며, 이 테넌트 전용 토큰을 요구한다.

### 기존 코드의 문제

```typescript
// BotFrameworkAdapter (기본값 = Multi-Tenant)
const adapter = new BotFrameworkAdapter({
  appId: process.env.MICROSOFT_APP_ID ?? '',
  appPassword: process.env.MICROSOFT_APP_PASSWORD ?? '',
  // channelAuthTenant 미설정 → botframework.com 테넌트 사용
});
```

`channelAuthTenant` 없이는 `botframework.com` 테넌트에서 토큰을 발급받는데, 이 토큰으로 테넌트별 엔드포인트에 요청하면 401이 반환된다.

## 해결책: CloudAdapter + SingleTenant 설정

`botbuilder` v4.14+의 `CloudAdapter`를 사용하면 Single-Tenant 설정을 명시적으로 지정할 수 있다.

```typescript
import { CloudAdapter, ConfigurationBotFrameworkAuthentication } from 'botbuilder';

const auth = new ConfigurationBotFrameworkAuthentication({
  MicrosoftAppId: process.env.MICROSOFT_APP_ID ?? '',
  MicrosoftAppPassword: process.env.MICROSOFT_APP_PASSWORD ?? '',
  MicrosoftAppType: 'SingleTenant',                          // 핵심
  MicrosoftAppTenantId: process.env.MICROSOFT_APP_TENANT_ID ?? '',
});

const adapter = new CloudAdapter(auth);
```

### Express 라우트 변경

```typescript
// 기존 (BotFrameworkAdapter)
app.post('/api/messages', (req, res) => {
  adapter.processActivity(req, res, async (context) => {
    await bot.run(context);
  });
});

// 변경 후 (CloudAdapter)
app.post('/api/messages', async (req, res) => {
  await adapter.process(req, res, async (context) => {
    await bot.run(context);
  });
});
```

## 비교 정리

| 구분 | BotFrameworkAdapter | CloudAdapter + SingleTenant |
|------|---------------------|---------------------------|
| Multi-Tenant 봇 | ✅ 정상 | ✅ 정상 |
| Single-Tenant 봇 (텍스트 응답) | ❌ 401 오류 | ✅ 정상 |
| Single-Tenant 봇 (카드 액션) | ✅ 정상 | ✅ 정상 |

**Single-Tenant Azure AD 앱으로 등록된 MS Teams 봇은 `CloudAdapter`를 사용하자.**

## 참고 자료

- [GitHub - MeaLOps](https://github.com/lim4349/mealops)
- [Azure Bot Service Authentication](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-concept-authentication)

## FAQ

- **BotFrameworkAdapter와 CloudAdapter의 차이는?**
  - `BotFrameworkAdapter`는 레거시 어댑터로 Multi-Tenant 기본 설정이다. `CloudAdapter`는 v4.14+에서 도입된 새 어댑터로 `MicrosoftAppType`을 통한 명시적 테넌트 설정을 지원한다.

- **serviceUrl이 뭔가요?**
  - Bot Connector Service의 엔드포인트 URL이다. 봇이 응답을 보낼 때 이 URL로 API 호출을 한다.

- **카드 액션은 왜 인증 없이 동작하나요?**
  - 카드 액션(`invoke`)은 Teams→봇으로 온 HTTP 요청에 대한 응답으로 직접 반환(`res.json()`)하기 때문이다. 반면 텍스트 응답은 별도의 아웃바운드 API 호출이 필요하다.
