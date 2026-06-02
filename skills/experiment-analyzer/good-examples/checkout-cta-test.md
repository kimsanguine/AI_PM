# Good 예시 — Checkout CTA A/B 분석

## 결론 (한 줄)

주 메트릭(checkout 완료율) +2.1% (p=0.012, n=8,420 per arm) — **ship 권고**.

## 무엇을 했나

- 변경: checkout 페이지의 CTA 문구 "Continue" → "Pay $X.XX securely"
- 기간: 2026-04-22 ~ 2026-05-13 (3주, novelty 통과)
- 표본: control n=8,420 / treatment n=8,395 (균형 양호, p=0.84)
- 가설: 가격·보안 신호를 CTA 에 노출하면 confidence ↑ → 완료율 ↑.

## 결과 표

| 메트릭 | Control | Treatment | Δ | p-value |
|---|---|---|---|---|
| Checkout 완료율 | 38.2% | 40.3% | +2.1pp | 0.012 |
| 평균 객단가 | $42.10 | $42.05 | -$0.05 | 0.79 |
| 환불율 (7일) | 2.4% | 2.5% | +0.1pp | 0.62 |

## 가드레일

- 환불율 (7일): 0.1pp 증가, p=0.62 — 변화 없음으로 판정.
- 평균 객단가: 변화 없음 — 가격 민감 segment 영향 없음.

## 의심 신호 (있다면)

- 표본 균형 OK (p=0.84).
- novelty 효과 가능성: 3주간 일별 추이 안정 — 통과.
- mobile / desktop segment 분리 시 mobile 만 +3.4%, desktop +0.8% — 핵심 임팩트는 mobile.

## 권고

**ship** (전체 트래픽으로 rollout).

- 사유: 비즈니스 임팩트 (월 +$NN 매출 추정), 가드레일 안전.
- 다음 step: mobile 변형 추가 실험, desktop 은 별도 가설 필요.
