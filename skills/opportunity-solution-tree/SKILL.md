---
name: opportunity-solution-tree
description: 하나의 outcome 에서 출발해 opportunity → solution → experiment 로 내려가는 트리를 만든다. opportunity 는 발견된 사용자 니즈/페인(솔루션 아님)으로만 적고, solution 은 opportunity 에 매달리며, 각 solution 은 검증 실험으로 닫는다. 출처는 Teresa Torres (Continuous Discovery Habits).
trigger: |
  "opportunity solution tree", "OST", "발견 트리", "outcome 에서 기회 나열", "솔루션 후보 정리", "어떤 실험부터" 요청 시.
model: claude-opus-4-8
---

# Skill — Opportunity Solution Tree (OST)

## Task

하나의 측정 가능한 outcome 을 루트로, **opportunity(기회) → solution(솔루션) → experiment(실험)** 4계층 트리를 출력한다. 트리는 의사결정 경로를 보이게 하는 것이 목적이다.

## Scope

- 트리 구성만. 실제 실험 실행·PRD 작성·우선순위 확정 commit 은 별도 단계.
- 입력은 합성된 discovery 인사이트(예: `discovery-synthesizer` 출력) 또는 사용자가 제시한 outcome + 인터뷰 근거.
- opportunity 는 **사용자 니즈/페인/욕구** 로만 적는다 — 솔루션·기능을 opportunity 자리에 넣지 않는다.
- 근거 없는 opportunity 는 "가설 opportunity" 로 표기.

## Length

- outcome 1개. opportunity 3–6개. opportunity 당 solution 1–3개. 선택된 solution 당 experiment 1–2개.
- 전체 1,500–3,000자.

## Format

1. `## Outcome (루트)` — 한 문장, 측정 가능한 product outcome (business metric 아님).
2. `## 트리` — 들여쓰기 목록 또는 표로 outcome → opportunity → solution → experiment 계층.
3. `## 이번에 집중할 가지` — 어느 opportunity 를 먼저 공략할지 + 근거(빈도/임팩트).
4. `## 첫 실험` — 가장 작은 검증 실험 1개: 가설 / 검증 방법 / 성공 기준 / 기각 기준.
5. `## 한계` — 미검증 opportunity, 근거 약한 가지, compare-and-contrast 누락 여부.

## 룰

- 출처 명시: OST 는 Teresa Torres 의 "Continuous Discovery Habits" 에서 정립된 도구다. 이론적 규칙(예: opportunity 는 솔루션이 아니다, solution 은 여러 개를 비교한다)을 인용할 때 출처를 적는다.
- outcome 은 **product outcome**(사용자 행동 변화)로. "매출 +20%" 같은 business outcome 은 루트로 쓰지 말고, 그것을 이끄는 product outcome 으로 환원.
- opportunity 는 사용자 언어로. "검색 기능" 은 solution. "원하는 항목을 빨리 못 찾는다" 가 opportunity.
- 한 opportunity 에 solution 을 최소 2개 두도록 권한다 — 단일 solution 은 비교 없는 commit 이다 (Torres 의 compare-and-contrast 원칙).
- experiment 는 가장 싼 것부터. "전부 만들어 본다" 는 experiment 가 아니다.
- 빈도·근거가 없는 opportunity 는 가설로 분리하고 트리 본문 우선순위에서 제외.

## 의존

- 입력 우선순위: `samples/user-survey-results.csv` (실습 데이터)
- 참고 챕터: `4.1-discovery-user-research.md`

## 예시

- 좋은 출력: `good-examples/ost-onboarding-activation.md`
- 나쁜 출력: `bad-examples/solution-as-opportunity.md`
