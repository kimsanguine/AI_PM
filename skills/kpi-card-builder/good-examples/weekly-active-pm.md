# Good 예시 — WAPM (Weekly Active PM) 카드

## KPI Card — Weekly Active PM (WAPM)

### 정의 (한 문장)

주간 7일 중 본 가이드의 `/today`, `/prd`, `/briefing` 중 1개 이상을 1회 이상 호출한 고유 PM 사용자 수.

### 계산식

```sql
SELECT COUNT(DISTINCT user_id)
FROM slash_command_events
WHERE command IN ('today', 'prd', 'briefing')
  AND ts >= DATE_TRUNC('week', CURRENT_DATE)
  AND ts <  DATE_TRUNC('week', CURRENT_DATE) + INTERVAL '7 days';
```

### Source

- 데이터 출처: `events.slash_command_events` (analytics DB)
- Owner of source: Data Platform 팀
- Refresh cadence: daily (월요일 아침 KPI freeze)

### 임계치 (반응 기준)

| Level | 값 | 행동 |
|---|---|---|
| Green | ≥ 400 | 정상 운영, 주간 보고 |
| Amber | 250–400 | 주간 review 추가, 이탈 원인 분석 |
| Red | < 250 | 즉시 product review, retention 디깅 |

### 소유자

- KPI Owner: @kimsanguine
- 백업: TBD
- review cadence: weekly (월 09:30 KPI sync)

### 반反사례 (이 KPI 가 잡지 못하는 것)

- 1회 사용 후 영영 안 돌아오는 사용자 → retention 으로 따로 봐야 함.
- 슬래시 외의 가이드 chapter md 읽기만 하는 사용자 → 별도 metric.
- 같은 사용자가 같은 슬래시를 100번 호출해도 1로 카운트됨 (depth 미반영).

### 의존 KPI

- 가드레일: **WAU retention 4주 (Active 4 of 4)** — 1회성 사용자 비율 견제.
- 가드레일: **/retro 실행률** — 폐루프 작동 여부 가늠.
- 함께 보는 supporting KPI: 슬래시별 호출 횟수, 평균 세션 길이.
