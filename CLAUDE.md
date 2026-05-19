# CLAUDE.md — AI_PM 가이드 (루트)

> 이 파일은 Claude Code가 본 레포에서 작업할 때의 행동 규칙입니다.
> 가이드 챕터 3.2 / 3.2.1 / 3.2.2 가 이 파일을 worked example 로 인용합니다.

---

## 1. Project — 정체성

- 본 레포는 **PM을 위한 Claude Code 실전 가이드**입니다.
- 1차 독자: 한국어 사용 PM (J/P/L 3레벨).
- 시리즈 정체성: AI_Human → AI_Engineer → **AI_PM** (실전).
- 자매 프로젝트: `kimsanguine/hplan` (Product Build Gate).

## 2. Conventions — 글쓰기 규칙

- 언어: 한국어 본문 + 필요한 영어 용어(원어 유지).
- 구조: H2/H3 + 짧은 표. 불릿 남발 금지. 한 절 = 한 주장.
- 코드/명령은 펜스 블록. 모델 ID는 `claude-opus-4-7` 정자.
- 모델 마케팅 이름(`Claude 4 Opus` 등) 사용 금지.
- 챕터 본문 분량 가이드: 8–25KB.

## 3. Workflows — 모든 슬래시/스킬에 4섹션 의무

모든 `templates/commands/*` 와 `skills/*/SKILL.md` 와 `.claude/agents/*` 는 다음 4섹션을 가집니다.

- **Task** — 무엇을 한다.
- **Scope** — 어디까지 한다, 어디는 안 한다.
- **Length** — 출력 길이 (예: 800–1200자).
- **Format** — 출력 포맷 (markdown / JSON / XML 등).

현재 자산 (참고):
- 슬래시 9종: `today`, `prd`, `status`, `discovery`, `competitor`, `briefing`, `review`, `postmortem`, `retro`
- 스킬 5종: `prd-generator`, `discovery-synthesizer`, `competitor-battlecard`, `experiment-analyzer`, `kpi-card-builder`
- 서브에이전트 3종: `engineering-reviewer`, `exec-advisor`, `user-researcher`
- 훅 3종: `stop-notify.sh`, `posttooluse-fmt.sh`, `sessionstart-load.sh`

## 4. Tools — 도구·모델

- 모델: `claude-opus-4-7`.
- effort: **xhigh** (편집/에이전트 작업), **high** (리뷰), **medium** (단순 lookup).
- thinking: adaptive (off-by-default). 다단계 추론이 필요할 때만 켠다.
- 컨텍스트: 1M. 안정 영역(이 파일, `INDEX.md`)을 상단에 둬 prompt caching 적중률을 높인다.
- MCP: Notion / GitHub / n8n. SoT 정책은 `docs/operations/sot-policy.md`.
- Hooks: `templates/hooks/` 의 3종 스크립트를 `~/.claude/hooks/` 로 복사하면 SessionStart / PostToolUse / Stop 폐루프가 작동.

## 5. Voice — 톤

- 직설적, 단정적. 검증되지 않은 주장은 "근거 없음"이라고 말한다.
- 과도한 이모지·과장된 형용사 금지. 결론을 첫 문장에 둔다.
- 사용자의 framing을 무조건 동의하지 않는다 — 동의하지 않으면 그 이유를 먼저 적는다.

## 6. Examples — 예시

- 모든 챕터·스킬·커맨드는 3–5개의 `<example>` 블록을 포함한다.
- good / bad 짝으로 제공한다. 단순 good만 있는 것보다 대비가 학습 효과를 높인다.
- 예시 입력은 `samples/` 파일을 우선 사용한다.

## 7. Escalation / Out-of-scope — 4.7 literal following 대응

- 일반화 금지: "Apply to every chapter"처럼 명시 scope가 없으면 한 챕터에만 적용한다.
- 본 레포 밖 작업 금지 (다른 레포 cross-edit 금지).
- 추측 금지: 사실/링크가 불확실하면 "확인 필요" 라벨을 단다.
- subagent fan-out 기준: 3개 이상 챕터 동시 검수, 6개 이상 파일 동시 grep 시에만.

## 8. Knowledge Map — 지식 진입점

- 모든 작업은 `INDEX.md` 를 먼저 읽고 관련 파일만 펼친다.
- 챕터는 `docs/partN-*/` 폴더 구조로 배치. README 의 목차가 진입점.
- 운영 문서: `docs/operations/` (SoT 정책 + 폐루프 운영).
- 변경 시 `CHANGELOG.md` 갱신 + 챕터 front-matter `last_updated` 갱신.
- CI 자동 검증: `.github/workflows/` (lint · links · frontmatter).

---

## 검증 사다리 (변경 후 항상 통과)

1. **자동 포맷** — markdownlint / textlint 통과
2. **링크** — 깨진 링크 0 (`lychee` 권장)
3. **시각** — README · 챕터 변경 시 GitHub 렌더링 확인
4. **LLM 리뷰** — 챕터 신설/대규모 개정 시 별도 세션 review

## 폐루프

- 주 1회 `/retro` 로 트랜스크립트 분석 (`templates/commands/retro.md`). 운영 가이드: `docs/operations/closed-loop.md`.
- 자주 고치는 항목은 본 파일 또는 스킬로 흡수. 한 번뿐인 지시는 흡수하지 않는다.
- 룰 중복 금지: **One rule = one place.**

---

last_updated: 2026-05-19
claude_model: claude-opus-4-7
guide_version: v1.2
