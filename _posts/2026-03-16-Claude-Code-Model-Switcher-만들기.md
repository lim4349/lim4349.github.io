---
title: Claude Code Model Switcher 만들기
date: 2026-03-16 15:00:00 +0900
categories: ['개발']
tags: ['claude-code', 'cli', 'bash', 'glm', 'kimi', 'llm']
author: lim4349
---

# Claude Code Model Switcher 만들기

Claude Code CLI를 쓰다 보니 다른 모델(GLM, Kimi)도 같은 방식으로 쓰고 싶어졌다. 그래서 모델 전환을 쉽게 해주는 래퍼 스크립트를 만들었다.

## 동기

매번 모델 바꾸는 게 귀찮았다. 특히:

- **Claude 기본**은 토큰 가격이 너무 비싸다
- **GLM**은 회사에서 결제해줘서 마음껏 쓸 수 있다
- **Kimi**는 1달 $0.99 프로모션으로 가성비가 좋다

이걸 쉽게 전환해서 쓰고 싶었다.

## 지원 모델

| 명령어 | 모델 | 제공업체 |
|--------|------|----------|
| `claude` | Claude Sonnet 4.5 | Anthropic |
| `claude-opus` | Claude Opus 4.6 | Anthropic |
| `claude-haiku` | Claude Haiku 4.5 | Anthropic |
| `claude-glm` | GLM 4.7 / 5 | Z.AI |
| `claude-kimi` | Kimi 2.5 | Moonshot AI |

## 사용법

### 설치

```bash
git clone https://github.com/lim4349/claude-code-model-switcher.git
cd claude-code-model-switcher
./install.sh
```

설치하면 API 키 설정과 `--dangerously-skip-permissions` 옵션을 물어본다.

### API 키 설정

```bash
claude-model setup
```

GLM, Kimi 중 원하는 모델의 API 키를 입력하면 된다.

### 실행

```bash
claude          # Claude Sonnet
claude-glm      # GLM (기본: glm-4.7)
claude-kimi     # Kimi 2.5
```

GLM은 내부에서 `/model glm-4.7` 또는 `/model glm-5`로 전환할 수 있다.

### 관리 명령어

```bash
claude-model setup      # API 키 설정
claude-model config     # 개별 모델 설정
claude-model current    # 현재 모델 확인
claude-model list       # 사용 가능한 모델 목록
```

---

## 구현 방식

### 래퍼 스크립트

각 명령어는 환경변수를 설정하고 원래 `claude` 바이너리를 실행하는 래퍼다.

```bash
# claude-glm 래퍼 예시
export CLAUDE_SETTINGS_FILE="$HOME/.claude/zai_settings.json"
exec "$CLAUDE_BIN" "$@"
```

### 설정 파일 구조

각 프로바이더별로 `~/.claude/{provider}_settings.json` 파일을 만든다.

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "...",
    "ANTHROPIC_MODEL": "glm-4.7",
    "CLAUDE_CODE_AVAILABLE_MODELS": "glm-4.7,glm-5"
  }
}
```

### 기존 claude 백업

이미 설치된 `claude` 바이너리가 있으면 `claude.original`로 백업해둔다. 삭제할 때 복구 가능.

---

## 개발하면서 겪은 문제들

### 1. Windows 버전

당연히 PowerShell 스크립트도 만들어야 했다. bash랑 문법이 완전히 달라서 귀찮았다.

### 2. Claude 바이너리 경로 찾기 (제일 열받은 부분)

회사 GPU 서버가 보안 때문에 바스티온 서버를 거쳐야 들어갈 수 있는 구조다. 그런데:

1. **root 파티션 용량이 너무 작음** - k3s, docker 다 안 됨
2. **overlayfs 버그** - NFS 마운트 공간에 docker 기본 폴더를 못 옮김
3. **모든 걸 데이터 디렉토리로 옮김** - claude 버전 관리도 거기서 됨

문제는 스크립트가 `$HOME/.local/share/claude/versions/`를 하드코딩으로 찾는다는 거다.

```bash
# _find_real_claude() 함수 내부
local versions_dir="$HOME/.local/share/claude/versions"
```

근데 실제로는 `/data/...` 같은 곳에 설치되어 있어서, `claude install`로 최신 버전을 받아도 스크립트는 구버전을 실행하는 상황이 발생했다.

**해결**: 심볼릭 링크로 우회.

```bash
mkdir -p ~/.local/share/claude
ln -s /data/actual/claude/versions ~/.local/share/claude/versions
```

이게 제일 열받았다. 경로를 환경변수로 받게 고치는 게 나을 것 같은데, 당장은 심볼릭 링크로 퉁쳤다.

### 3. Text file busy

실행 중인 스크립트를 덮어쓰려니 `cp: text file busy` 에러가 났다. 임시 파일 만들고 `mv`로 원자적 교체하는 방식으로 해결.

```bash
tmp=$(mktemp)
cp "$source" "$tmp"
chmod +x "$tmp"
mv -f "$tmp" "$target"
```

### 4. bash 3.2 호환성

macOS 기본 bash가 3.2라 `[[ -v var ]]` 같은 문법을 못 쓴다. `[[ -n "${var:-}" ]]`로 우회.

---

## API 키 발급처

| 제공업체 | 링크 |
|----------|------|
| **Claude** | https://console.anthropic.com/ |
| **GLM** | https://open.bigmodel.cn/ |
| **Kimi** | https://platform.moonshot.ai/ |

---

## 참고 자료

- [GitHub - claude-code-model-switcher](https://github.com/lim4349/claude-code-model-switcher)
- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code)

---

## 총평

**좋았던 점**:
- 한번 API 키 등록해두면 `claude-glm`, `claude-kimi`로 바로 실행 가능
- bash로만 짜서 의존성이 없다
- Windows(PowerShell)도 지원한다

**아쉬웠던 점**:
- 새 모델이 나오면 `base_url`과 정확한 모델명을 찾아서 넣어야 한다
- GLM, Kimi가 Claude Code API를 완벽히 호환하지 않아 가끔 이상 동작한다
- 바이너리 경로가 하드코딩이라 비표준 위치에 설치하면 삽질해야 함

**결론**: 한번 세팅해두면 편하다. 특히 회사에서 GLM 결제해주거나 Kimi 프로모션 쓸 때 유용하다.
