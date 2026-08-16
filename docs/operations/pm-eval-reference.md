# PM-Eval 참고표: 제품 간 운영모델 검토

> 이 참고표는 hplan, signal-to-growth, AI_PM, AI PM Plane을 함께 쓰는 PM이
> 책임 경계와 검토 품질을 점검하도록 돕는다. 별도 원장, 자동 의사결정, 외부
> 시스템 쓰기 기능은 만들지 않는다.

## 1. 언제 사용하는가

handoff를 도입하거나 운영 회고를 할 때, 담당 PM은 source system의 원문을
열어 본 뒤 이 참고표로 **운영 방식**을 평가한다. 이 결과는 평가 메모일 뿐
Build Gate나 성장 outcome을 변경하는 명령이 아니다.

공개 예시는 합성 Profile v0와 opaque reference만 사용한다. 고객 신호,
evidence 본문, metric 값, source decision 본문을 AI_PM에 복사하지 않는다.

## 2. 100점 참고표

| 기준 | 배점 | 25점/만점 상태 | 0점 상태 |
| --- | ---: | --- | --- |
| Source ownership | 25 | hplan은 Gate, signal-to-growth는 신호·실험·metric·outcome, Plane은 정책·승인·감사를 각각 소유하며 AI_PM은 교육·평가만 담당한다. | 다른 제품의 Gate, metric, evidence, approval을 자신의 정본으로 기록하거나 다시 쓴다. |
| Evidence quality | 25 | 모든 handoff에 Profile v0, stable opaque source reference, named owner, `review_at`이 있고 재검토 요청에는 `reopen_reason`이 있다. | 참조가 없어 원문을 찾을 수 없거나, 복사한 값·원문으로 source를 대체한다. |
| Human approval | 25 | 사람의 확인 지점과 책임자가 명시되어 있으며, fixture release의 Plane은 `approved_write`를 실행하지 않는다. 이후 외부 write가 검토되더라도 기록된 사람 승인이 먼저 필요하다. | 에이전트가 사람 승인 없이 외부에 쓰거나 승인 receipt를 생략한다. |
| No-auto-decision | 25 | outcome은 재검토 요청만 만들고, 새 `GO`·`HOLD`·`INVESTIGATE`는 hplan에서 사람이 결정한다. | outcome·점수·모델 응답이 Gate 또는 성장 결과를 자동 변경한다. |

**판정 가이드:** 90점 이상은 도입 후보, 70–89점은 결손 기준을 보완한 뒤
재검토, 69점 이하는 source 경계부터 다시 설계한다. 단, 표의 0점 상태가 하나라도
있으면 총점과 무관하게 보류한다. 이 점수는 사람의 운영 판단을 돕는 참고값이다.

## 3. 합성 루프를 평가하는 방법

다음 네 줄을 source record의 내용 대신 확인한다. 식별자는 모두 공개 fixture의
opaque reference다.

1. hplan의 `hplan://checkpoint/CP-0001`이 `GO`를 source-native로 확정하고,
   Profile v0로 `build_gate_to_growth` 참조만 전달했는가?
2. signal-to-growth가 `stg://experiment/EXP-0001`의 실험을 소유하고, metric
   본문이나 결과값을 handoff에 복제하지 않았는가?
3. signal-to-growth가 `stg://outcome/OUT-0001`에서
   `growth_outcome_to_reconsideration`을 만들 때 `reopen_reason`, owner,
   review 시점을 제공했는가?
4. 사람이 hplan을 다시 열어 판단했는가? 그렇지 않다면 루프는
   reconsideration 요청에서 멈춘 것으로 기록하고 결론을 추정하지 않는다.

## 4. 평가 메모 템플릿

```markdown
## PM-Eval — <project_id>

- 범위: <검토한 handoff / 운영 흐름>
- source references: <opaque ref 목록; 원문·값을 복사하지 않음>
- ownership (0–25): <근거와 점수>
- evidence quality (0–25): <근거와 점수>
- human approval (0–25): <근거와 점수>
- no-auto-decision (0–25): <근거와 점수>
- 합계: <0–100>
- 사람의 다음 검토: <담당자와 review_at>
- 이 메모가 바꾼 source record: 없음
```

AI_PM은 이 메모를 교육용 artifact로만 취급한다. 실제 Gate, experiment,
metric, approval receipt는 해당 source system에서 확인하고 변경한다.

---

last_updated: 2026-08-17
