---
name: competitor-battlecard
description: 경쟁사 3–5곳을 동일 축으로 비교한 표 + 배틀카드를 생성한다. 정량/공개 자료만 근거로 사용하고, 추측이나 미확인 정보는 한계 절에 분리한다.
trigger: |
  "경쟁사 분석", "battlecard 만들어", "competitor 비교", "포지셔닝 표" 요청 시.
model: claude-opus-4-8
---

# Skill — Competitor Battlecard

## Task

지정된 경쟁사 3–5곳에 대해 **동일 축의 비교 표 + 경쟁사별 배틀카드** 를 출력한다.

## Scope

- 정량·공개 자료(가격·기능·리뷰 별점·MAU 공시·언론 보도)만 근거.
- 입력: `samples/competitor-data.json` 또는 사용자가 첨부한 자료.
- 출력은 표 + 배틀카드까지. GTM 전략 변경·실제 메시지 작성은 별도 단계.

## Length

- 비교 표 5–8행, 3–5열. 배틀카드 한 경쟁사당 ≤ 300자.
- 전체 1,500–3,000자.

## Format

1. `## 비교 축` — 표 (Target / Core feature / Price / Strength / Weakness 등).
2. `## 배틀카드 — 경쟁사 A` — 강점/약점/우리의 differentiator/그들의 공격→우리의 응답.
3. `## 한계` — 자료 freshness, 누락 경쟁사, 추가 조사 필요.

## 룰

- 추측 금지. 자료 없는 셀은 "—" + 한계 절에 명시.
- "우리가 더 낫다" 같은 단정은 비교 축의 근거가 있을 때만.
- 자료 freshness 6개월 초과 항목은 [stale] 태그.
- 배틀카드의 "그들의 공격" 절은 **실제 영업 현장에서 나올 만한 문장** 으로 작성.

## 의존

- 입력 우선순위: `samples/competitor-data.json`
- 참고 챕터: `4.2-discovery-competitive-analysis.md`, `A.6-usecase-battle-cards.md`

## 예시

- 좋은 출력: `good-examples/pm-tool-3way.md`
- 나쁜 출력: `bad-examples/unsourced-claims.md`
