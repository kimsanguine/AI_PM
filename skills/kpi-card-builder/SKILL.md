---
name: kpi-card-builder
description: "KPI 1개에 대한 정의 카드(이름·계산식·source·반응 임계치·소유자·반反사례) 를 생성한다. 한 카드 = 한 KPI 룰을 강제하고 KPI 가 측정 불가하면 정의를 거부한다."
trigger: |
  "KPI 정의해줘", "이 지표 어떻게 측정해", "정의 카드 만들어" 요청 시.
model: claude-opus-4-7
---

# Skill — KPI Card Builder

## Task
하나의 KPI 에 대해 **정의 카드(definition card)** 를 생성한다. 측정 불가능하거나 ambiguous 하면 카드 작성을 거부하고 명확화 질문을 한다.

## Scope
- 한 카드 = 한 KPI. 여러 KPI 를 묶지 않는다.
- 입력: KPI 이름 + 비즈니스 컨텍스트.
- 측정 불가능한 KPI ("사용자 만족", "혁신 정도") 는 작성 거부 + 측정 가능 형태로 재정의 제안.

## Length
- 카드 1개당 600–1,200자.

## Format
```markdown
## KPI Card — <이름>

### 정의 (한 문장)
<무엇을 측정하는지>

### 계산식
```
<수식 또는 SQL pseudo-code>
```

### Source
- 데이터 출처: <시스템 / 테이블>
- Owner of source: <팀>
- Refresh cadence: <daily / weekly / real-time>

### 임계치 (반응 기준)
| Level | 값 | 행동 |
|---|---|---|
| Green | ≥ X | 정상 운영 |
| Amber | X–Y | 주간 review 추가 |
| Red | < Y | 즉시 incident 대응 |

### 소유자
- KPI Owner: <PM 이름>
- 백업: <이름>
- review cadence: <weekly / monthly>

### 반反사례 (이 KPI 가 잡지 못하는 것)
- ...
- ...

### 의존 KPI
- 함께 봐야 하는 가드레일 KPI: <목록>
```

## 룰

- 측정 불가능한 KPI 는 작성 거부 — "측정 가능한 형태로 재정의해라" + 후보 3개 제안.
- 계산식이 ambiguous 하면 "이 부분 명확화 필요" 절을 둔다.
- 반反사례 절 없는 카드는 미완성 — 항상 적는다.
- KPI 1개가 너무 많은 것을 잡으려 하면 "분리하라" 권고.
- "사용자 만족도" 같은 마법 단어는 NPS / CSAT / 이탈율 / 재방문 등 측정 가능 형태로 분해.

## 의존
- 참고 챕터: `7.2-growth-kpi-dashboard.md`
- 참고 가이드: `~/.claude/guides/evals.md`

## 예시
- 좋은 출력: `good-examples/weekly-active-pm.md`
- 나쁜 출력: `bad-examples/user-satisfaction-vague.md`
