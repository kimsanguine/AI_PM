---
name: experiment-analyzer
description: A/B 테스트·실험 결과 CSV/표를 받아 PM 보고용 결과 절 + ship/iterate/kill 권고를 출력한다. 가드레일 위반·표본 편향·novelty 효과를 항상 점검한다.
trigger: |
  "A/B 결과 분석", "실험 결과 봐줘", "ship 해야 하나", "통계적으로 유의해?" 요청 시.
model: claude-opus-4-8
---

# Skill — Experiment Analyzer

## Task

실험 결과 데이터(CSV / 표)를 받아 **PM 보고 포맷** 으로 분석 결과 + ship/iterate/kill 권고를 출력한다.

## Scope

- 통계 분석 + 비즈니스 권고. 실제 ship 의사결정은 PM 의 몫.
- 입력: `samples/ab-test-results.csv` 또는 사용자 첨부.
- 한국어 보고 포맷 (`~/.claude/guides/evals.md` 의 PM 보고 포맷 따름).

## Length

- 결론 1줄 + 결과 표 + 가드레일 절 + 권고. 전체 1,000–2,000자.

## Format

```markdown
## 결론 (한 줄)
주 메트릭 +X.X% (p=0.0XX, n=NNN per arm) — ship / iterate / kill / extend

## 무엇을 했나
- 변경: <한 줄>
- 기간: YYYY-MM-DD ~ YYYY-MM-DD
- 표본: control n=NNN / treatment n=NNN
- 가설: <한 줄>

## 결과 표
| 메트릭 | Control | Treatment | Δ | p-value |
|---|---|---|---|---|

## 가드레일
- 메트릭 X: 변화 없음 / 악화 -X.X%
- 메트릭 Y: ...

## 의심 신호 (있다면)
- 표본 균형 / novelty / segment 편향 / Simpson's paradox 검토 결과.

## 권고
ship / iterate / kill / extend
- 사유: <한 줄>
- 다음 step: <한 줄>
```

## 룰

- p<0.05 인데 effect size 가 사실상 0 이면 **ship 권고 금지** — "통계적 유의" 와 "비즈니스 의미" 를 분리.
- 가드레일이 무너졌으면 주 메트릭 결과와 무관하게 **ship 권고 금지**.
- p-hacking 의심 신호 (subgroup 6개 검사 후 1개 채택) 발견 시 명시.
- novelty 효과 가능성 (1주 미만 데이터) 명시.
- "감으로는 좋아 보임" 추가 금지. 정량 외 의견 금지.

## 의존

- 입력: `samples/ab-test-results.csv`
- 참고 가이드: `~/.claude/guides/evals.md`
- 참고 챕터: `7.1-growth-experiment-analysis.md`

## 예시

- 좋은 출력: `good-examples/checkout-cta-test.md`
- 나쁜 출력: `bad-examples/p-only-recommend.md`
