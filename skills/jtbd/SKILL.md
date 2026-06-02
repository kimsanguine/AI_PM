---
name: jtbd
description: 인터뷰·기능 요청을 "사람들이 해결하려는 job(과업)" 으로 재구성한다. 기능·솔루션 언어를 상황(when)·동기(want)·기대 결과(so I can) 의 job statement 로 환원하고, 근거 없는 job 은 가설로만 표기한다. 출처는 Clayton Christensen / Anthony Ulwick.
trigger: |
  "JTBD", "Jobs to be Done", "job statement", "고객이 왜 산다", "기능 요청을 재해석", "이 기능 진짜 필요한가" 요청 시.
model: claude-opus-4-8
---

# Skill — Jobs-to-be-Done (JTBD)

## Task

인터뷰 발화·기능 요청·사용 로그를 받아, 사용자가 실제로 해결하려는 **job(과업) 으로 재구성한 job statement + job map + 한계 절** 을 출력한다.

## Scope

- 재구성만. PRD 작성·우선순위 결정·솔루션 설계는 별도 단계.
- 입력은 `samples/*.csv|*.json`, `@<path>`, 또는 본문에 붙여넣은 인터뷰/요청 텍스트.
- 솔루션 언어("드롭다운 추가", "엑셀 내보내기")는 그 자체를 job 으로 쓰지 않는다 — 그 솔루션이 끝내려는 job 으로 한 단계 올린다.
- 근거가 N=1~2 면 job 이 아니라 "가설 job" 으로만 표기.

## Length

- job statement 3–7개. 각 statement 는 한 문장 + 근거 quote 2–3개 + 현재 해결책 + 미충족 정도.
- 전체 1,500–3,000자.

## Format

1. `## Job statement 1 — <상황일 때, 나는 ~하고 싶다, 그래서 ~할 수 있다>` — 근거 quote / 현재 사용하는 해결책(hire) / 미충족 정도(under/over-served) / push·pull·anxiety·habit 4요인 중 관찰된 것.
2. `## Job map` — job 의 단계(define → locate → prepare → confirm → execute → monitor → conclude) 중 마찰이 큰 단계 표.
3. `## 가설 job (참고용)` — N<3 으로 확정 못 한 job.
4. `## 한계` — 표본 편향, 솔루션-job 혼동 위험, 추가 인터뷰 필요.

## 룰

- 출처 명시: JTBD 는 Clayton Christensen 의 "milkshake" 사례와 Anthony Ulwick 의 Outcome-Driven Innovation 에서 정립된 프레임이다. 이론적 주장을 인용할 때 둘 중 어느 계열인지 적는다.
- job statement 는 **솔루션 중립** 으로 적는다. "버튼", "화면", "AI" 같은 솔루션 명사가 들어가면 한 단계 올려 다시 적는다.
- "고객이 X 를 원한다" 가 아니라 "X 한 상황에서 고객은 Y 라는 진전을 원한다(progress)" 형식.
- 인터뷰 quote 는 그대로 인용. 손대지 않는다.
- 기능 요청은 "왜 그것을 요청했는가" 의 job 으로 환원하되, 환원이 추측이면 가설 job 으로 분리.
- "혁신적", "차별화된" 같은 형용사로 job 을 포장하지 않는다.

## 의존

- 입력 우선순위: `samples/user-survey-results.csv` (실습 데이터)
- 참고 챕터: `4.1-discovery-user-research.md`

## 예시

- 좋은 출력: `good-examples/jtbd-commute-coffee.md`
- 나쁜 출력: `bad-examples/feature-as-job.md`
