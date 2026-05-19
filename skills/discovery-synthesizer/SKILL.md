---
name: discovery-synthesizer
description: 인터뷰 트랜스크립트·설문·사용 로그를 받아 PM 이 의사결정할 수 있는 인사이트 표로 합성한다. 빈도가 낮은 신호는 "약한 신호" 로만 표기하고 인사이트로 승격하지 않는다.
trigger: |
  사용자가 인터뷰·설문·사용 로그 파일을 첨부하면서 "합성", "정리", "인사이트", "패턴 찾아줘" 라고 요청할 때.
model: claude-opus-4-7
---

# Skill — Discovery Synthesizer

## Task
첨부된 정성/정량 데이터를 합성해 **인사이트 3–7개 + 합성 표 + 한계 절** 을 출력한다.

## Scope
- 합성만. PRD 작성·로드맵·실험 설계는 별도 단계.
- 입력은 `samples/*.csv|*.json`, `@<path>`, 또는 사용자가 본문에 붙여넣은 트랜스크립트.
- N=1~2 패턴은 "약한 신호" 로만 표기 — 절대 "인사이트" 로 승격하지 않는다.

## Length
- 인사이트 3–7개. 각 인사이트는 한 문장 + 근거 quote 3개 + so-what 한 줄.
- 전체 1,500–3,000자.

## Format
1. `## 인사이트 1 — <한 문장>` — 빈도 / quote 3개 / so-what / 가설.
2. `## 합성 표` — 인사이트 vs 우선순위 (5열).
3. `## 약한 신호 (참고용)` — N<3 패턴들.
4. `## 한계` — 표본 편향, 신뢰, 추가 조사 필요.

## 룰

- 인터뷰 quote 는 그대로 인용. 손대지 않는다.
- "다양한", "여러", "효과적" 같은 무의미 형용사 금지. 숫자로.
- 한 인사이트는 한 문장으로 압축. 두 문장이면 인사이트가 두 개다.
- 표본이 한 segment 에 쏠려 있으면 "한계" 절에 반드시 명시.
- PM 의 confirmation bias 에 동의하지 않는다 — 데이터가 반대면 그렇게 말한다.

## 의존
- 입력 우선순위: `samples/user-survey-results.csv` (실습 데이터)
- 참고 가이드: `~/.claude/guides/evals.md` (lazy load)
- 참고 챕터: `4.1-discovery-user-research.md`

## 예시
- 좋은 출력: `good-examples/synthesis-pm-time.md`
- 나쁜 출력: `bad-examples/vague-themes.md`
