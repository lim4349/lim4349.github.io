---
title: 입력시 텍스트, 이미지 순서
date: 2025-11-20 09:15:00 +0900
categories: ['정리']
tags: ['ai', 'multimodal', 'vllm']
author: lim4349
---

# 입력시 텍스트, 이미지 순서

OpenCUA 모델을 vLLM 지원하기 위해 구현하다가 발견한 문제입니다.

## 문제 원인

Hugging Face에 명시된 예시 코드는 이미지 → 텍스트 순서로 되어 있습니다:

```python
"role": "user",
"content": [
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encode_image(image_path)}"}},
    {"type": "text", "text": instruction},
]
```

하지만 Cursor에 curl 명령어를 만들어달라고 요청했을 때, 텍스트 → 이미지 순서로 생성되었습니다:

```python
"role": "user",
"content": [
    {"type": "text", "text": instruction},
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encode_image(image_path)}"}},
]
```

입력 순서가 바뀌면서 결과에 큰 차이가 발생했습니다.

### 정상 동작 (이미지 → 텍스트 순서)

```
Test 1 Analysis (with system prompt):
  Instruction: Close the file explorer
  Response: ## Code:
  pyautogui.click(x=1424, y=264)

  Instruction: Open Recycle Bin
  Response: ## Code:
  pyautogui.click(x=39, y=146)
```

좌표가 정확하게 출력되며, 각 명령어에 따라 다른 좌표를 반환합니다.

### 비정상 동작 (텍스트 → 이미지 순서)

```
Test 1 Analysis (with system prompt):
  Instruction: Close the file explorer
  Response: ## Code:
  pyautogui.click(x=377, y=823)

  Instruction: Open Recycle Bin
  Response: ## Code:
  pyautogui.click(x=375, y=823)
```

모든 명령어에 대해 거의 동일한 좌표만 출력되며, 입력 텍스트를 변경해도 좌표가 변하지 않습니다.

### 문제의 특이점

흥미롭게도 이미지 캡셔닝(Captioning) 품질에서는 두 순서 간 차이를 구별하기 어렵지만, 모델의 핵심 기능인 좌표 출력에서만 문제가 발생합니다. 어떤 텍스트 입력으로 바꿔도 똑같은 좌표만 출력되어, position 관련 문제로 오해하고 약 1주일 동안 헤맸습니다.

## 해결 방법

### 방법: Hugging Face 예시 코드 순서 준수

Hugging Face에 명시된 예시 코드의 순서를 정확히 따르세요. 이미지 → 텍스트 순서로 입력해야 합니다.

```python
"role": "user",
"content": [
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encode_image(image_path)}"}},
    {"type": "text", "text": instruction},
]
```

**교훈**: AI 도구가 생성한 코드도 항상 검증하고, 공식 문서의 예시 코드를 우선적으로 따르는 것이 중요합니다.




## FAQ

- **순서가 바뀌면 왜 문제가 생기나요?**: 멀티모달 모델은 입력 순서에 따라 attention 메커니즘이 다르게 작동합니다. 이미지를 먼저 처리한 후 텍스트를 처리하는 것이 모델의 학습 방식과 일치하여 정확한 좌표 출력이 가능합니다. 반대로 텍스트를 먼저 처리하면 이미지 컨텍스트가 제대로 반영되지 않아 좌표 추출에 실패합니다. 