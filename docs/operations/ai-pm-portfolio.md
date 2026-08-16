# AI PM 포트폴리오 참조 운영

> hplan, signal-to-growth, AI_PM, AI PM Plane의 책임을 분리한 채 제품 판단의 근거를 참조로 연결한다.

## 1. 제품별 책임

네 제품은 하나의 런타임이나 통합 원장이 아니다. 각 제품은 자기 정본(Source of Truth)을 유지한다.

| 제품 | 책임 | 소유하지 않는 것 |
| --- | --- | --- |
| hplan | 빌드 전 투자 검토와 `GO`·`HOLD`·`INVESTIGATE` Build Gate 판단 | 성장 실험과 조직 접근 정책 |
| signal-to-growth | 고객 신호, 성장 실험, metric contract, 성장 outcome | Build Gate 판단 권한 |
| AI_PM | 운영 모델 교육, 역할 playbook, 교차 제품 예시, PM 평가 | 별도의 증거·판단 원장 |
| AI PM Plane (fixture-only) | 향후 조직 정책, 읽기·쓰기 권한, 승인 receipt, audit trail | 제품 판단 또는 성장 원장의 정본 |

## 2. 읽기 전용 참조 루프

최초 연동은 아래 참조 루프만 다룬다.

```text
hplan Build Gate
  -> 승인된 checkpoint 참조
  -> signal-to-growth experiment
  -> experiment, metric, outcome 참조
  -> hplan reconsideration 요청
  -> 사람의 새로운 hplan 판단
```

handoff는 읽기 전용이다. source-system의 판단을 변경하지 않으며, 다른 제품의 증거·metric·판단 본문을 복제하지 않는다. 수신 제품은 opaque reference만 보관하고, 사람의 검토 없이 `GO`·`HOLD`·`INVESTIGATE` 또는 성장 outcome을 다시 쓰지 않는다.

## 3. Handoff Profile v0

`contracts/ai-pm-handoff-profile-v0.schema.json`은 버전 `0.1` envelope를 정의한다. 현재 source system은 `hplan`과 `signal-to-growth`, handoff kind는 `build_gate_to_growth`와 `growth_outcome_to_reconsideration`만 허용한다. 후자는 사람이 재검토 이유를 이해하도록 비어 있지 않은 `reopen_reason`을 요구한다.

공개 fixture는 모두 합성 데이터이며 고객 데이터, 원문 인용, metric 값, source decision 본문을 포함하지 않는다. validator는 Python 표준 라이브러리만 사용한다.

```bash
python3 scripts/validate_handoff_profile.py \
  contracts/fixtures/hplan-build-gate-to-growth.valid.json
python3 scripts/validate_handoff_profile.py \
  contracts/fixtures/growth-outcome-to-reconsideration.valid.json
```

다음 두 명령은 의도적으로 exit code `1`을 반환하며, 각각 `reopen_reason`과 `profile_version` 오류를 stderr에 한 줄로 출력한다.

```bash
python3 scripts/validate_handoff_profile.py \
  contracts/fixtures/growth-outcome-missing-reopen-reason.invalid.json
python3 scripts/validate_handoff_profile.py \
  contracts/fixtures/unsupported-profile-version.invalid.json
```

## 4. 향후 AI PM Plane action class

fixture-only Plane은 정책 계약을 설명할 뿐 실제 외부 시스템에 쓰지 않는다.

| action class | 의미 | fixture release 기본값 |
| --- | --- | --- |
| `read` | 정책이 허용한 source를 읽는다 | 허용 규칙이 없으면 거부 |
| `draft` | 외부에 반영되지 않는 로컬 artifact를 만든다 | source policy가 있을 때만 허용 |
| `propose_write` | 대상별 외부 변경안을 준비한다 | 제안만 생성하고 쓰지 않음 |
| `approved_write` | 기록된 사람 승인 뒤 외부 변경을 실행한다 | fixture release에서는 거부 |

모든 외부 write는 현재 범위 밖이다. Linear, Notion, Jira, Slack, CRM을 포함한 실제 시스템의 쓰기 경로와 고객 데이터는 연결하지 않는다.

---

last_updated: 2026-08-16
