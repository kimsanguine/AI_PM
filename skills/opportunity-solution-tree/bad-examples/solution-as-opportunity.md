# Bad 예시 — 솔루션을 opportunity 자리에 넣은 트리

## 무엇이 문제인가

- opportunity 노드에 기능명(솔루션)이 들어감 → 트리가 "기능 목록" 으로 붕괴
- 루트가 product outcome 이 아니라 business 매출
- opportunity 당 solution 이 1개뿐 → 비교 없는 commit (Torres 의 compare-and-contrast 위반)
- experiment 가 "다 만들어서 본다" → 실험이 아님
- 빈도·근거 없음 → 어느 가지부터 할지 판단 불가

## 출력 (이렇게 하지 말 것)

- Outcome: 매출 20% 증가
  - Opportunity: 온보딩 튜토리얼 추가
    - Solution: 튜토리얼을 만든다
      - Experiment: 튜토리얼을 출시하고 매출을 본다
  - Opportunity: 다크 모드
    - Solution: 다크 모드를 만든다

## 왜 나쁜가

- "온보딩 튜토리얼 추가" 는 solution 이지 opportunity 가 아님. opportunity 는 "신규 사용자가 무엇부터 할지 모른다" 같은 **니즈** 여야 함.
- 루트가 "매출 20%" — business outcome 은 product outcome(사용자 행동 변화)으로 환원해야 트리가 작동.
- solution 이 opportunity 당 1개라 "다른 방법은 없었나" 를 영영 못 물음.
- "출시하고 매출을 본다" 는 통제 없는 관찰일 뿐 → 가설/성공 기준/기각 기준이 없는 가짜 실험.
- 빈도가 없어 다크 모드와 온보딩 중 무엇이 더 급한지 알 수 없음.
