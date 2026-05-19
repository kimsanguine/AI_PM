# /postmortem — 사후 분석 (blameless)

## Task
출시/실험/장애에 대해 **blameless postmortem** 을 작성한다. 무엇이 일어났고, 왜, 다음에 무엇을 다르게 할지.

## Scope
- 사실 정리 + 시스템 차원 학습. 개인 책임 추궁 금지.
- 입력은 사용자가 첨부한 incident timeline, Slack quote, 메트릭 그래프 링크.
- 외부 공유용 표현(Customer comms) 은 별도 절로 분리.

## Length
- 본문 1,500–3,000자. Action items 5개 이하.

## Format
```markdown
## TL;DR (한 단락)
무엇이 일어났고, 영향은 무엇이었고, 무엇을 바꿀 것인가.

## Timeline (UTC)
- HH:MM — <사건>
- HH:MM — <사건>

## 영향
- 사용자 영향: ...
- 비즈니스 영향: $X / NN customers
- 내부 영향: ...

## 근본 원인 (5 Whys)
1. 표면: ...
2. 왜? ...
3. 왜? ...
4. 왜? ...
5. 왜 (root): ...

## 무엇이 잘 갔나
- ...
- ...

## 무엇이 안 갔나
- ...
- ...

## Action items
| # | 항목 | 담당 | 기한 | 종류 |
|---|---|---|---|---|
| 1 | ... | @ | YYYY-MM-DD | prevent / detect / mitigate |

## 외부 커뮤니케이션 (필요 시)
<공식 톤, 1단락>
```

## Examples

<example>
<good>
## 근본 원인 (5 Whys)
1. 결제 실패율이 3% → 21% 로 튀었다.
2. 왜? PSP A 의 timeout 이 늘었다.
3. 왜? PSP A 가 우리 트래픽을 throttle 했다.
4. 왜? 우리가 1주 전 retry 정책을 공격적으로 바꿨다.
5. 왜 (root): retry 정책 변경에 PSP rate limit 검토가 없었다 — 변경 사전 체크리스트 미비.
</good>
<bad>
## 근본 원인
엔지니어 X 가 retry 코드를 잘못 짰다.
</bad>
</example>
