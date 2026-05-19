# ~/.claude/guides/evals.md (lazy reference)

> A/B 테스트 결과 분석·실험 평가·KPI 검토할 때만 모델이 펼친다.

---

## 분석 전 체크리스트

- 표본 크기와 통계적 검정력은? (n, MDE)
- 노출 / 전환의 정의가 모호하지 않은가?
- 가드레일 메트릭이 있는가? (주 메트릭만 보지 말 것)
- novelty / primacy effect 가능성 — 며칠 데이터인가?

## 보고 포맷 (PM 보고용)

```
## 결론 (한 줄)
주 메트릭 +X.X% (p=0.0XX, n=NNN per arm)

## 무엇을 했나
- 변경: <한 줄>
- 기간: YYYY-MM-DD ~ YYYY-MM-DD
- 표본: control n=NNN / treatment n=NNN

## 결과 표
| 메트릭 | Control | Treatment | Δ | p-value |

## 가드레일
- 메트릭 X: 변화 없음 / 악화 -X.X%

## 권고
- ship / iterate / kill / extend
- 근거: <한 줄>
```

## 의심 신호

- p<0.05 인데 effect size 가 사실상 0
- 표본이 한쪽으로 쏠림 (랜덤화 오류)
- 한 segment 가 결과를 끌고 감 (Simpson's paradox)
- 가드레일이 무너졌는데 주 메트릭만 보고 ship 추천

## 안티패턴

- "통계적으로 유의하다" 한 줄만 → 비즈니스 의미 없는 답
- p-hacking (subgroup 6개 검사 후 1개 채택)
- "감으로는 좋아 보임" 추가 — 정량 결과의 신뢰를 깎는다

---

last_updated: 2026-05-19
