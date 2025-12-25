---
title: "AttributeError: OpenCUAForConditionalGeneration object has no attribute _supports_sdpa"
date: 2025-11-03 09:15:00 +0900
categories:
  - 정리
tags:
  - ai
author: lim4349
---

# AttributeError: 'OpenCUAForConditionalGeneration' object has no attribute '_supports_sdpa'

OpenCUA 모델을 맥북에서 실행하다가 만난 에러입니다.

## 문제 원인

Transformers가 내부에서 SDPA(Scaled Dot-Product Attention) 지원 여부를 `_supports_sdpa` 속성으로 확인하도록 변경되었는데, 커스텀 모델 클래스(`OpenCUAForConditionalGeneration`)에 이 속성이 정의되어 있지 않아 발생한 에러입니다.

**참고**: [GitHub 이슈 #39974](https://github.com/huggingface/transformers/issues/39974)

## 해결 방법

### 방법 1: `_supports_sdpa` 속성 정의 (권장)

가장 근본적인 해결 방법입니다. 32B 최신 모델에는 이미 정의되어 있습니다.

```python
@property
def _supports_sdpa(self):
    """
    Retrieve language_model's attribute to check whether the model supports
    SDPA or not.
    """
    return self.language_model._supports_sdpa
```

### 방법 2: Eager 모드로 강제 설정

SDPA 경로를 사용하지 않도록 로딩 시점에 `eager` 모드로 강제 설정합니다.

#### 모델 로딩 시점에 설정

```python
model = OpenCUAForConditionalGeneration.from_pretrained(
    path_or_id,
    trust_remote_code=True,         # 사용 중이라면 유지
    attn_implementation="eager"     # 핵심
)
```

#### 이미 로드한 모델에 적용

```python
model.config._attn_implementation = "eager"
```

## FAQ

- **SDPA가 뭔데?**: Scaled Dot-Product Attention의 약자로, 더 효율적인 어텐션 메커니즘 구현 방식
- **Eager가 뭔데?**: 기본적인 어텐션 구현 방식으로, SDPA보다는 느리지만 더 안정적