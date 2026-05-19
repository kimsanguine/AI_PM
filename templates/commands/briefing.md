# /briefing — 일일 크로스 툴 브리핑

## Task
연결된 도구(Slack / Linear / Notion / GitHub / 캘린더)에서 어제~오늘의 신호를 모아 **PM 의 오늘 우선순위 5개** 로 압축 출력한다.

## Scope
- 데이터 수집·정렬만 한다. 결정·답장·이슈 생성은 하지 않는다.
- 시간 범위: 기본 24시간. 사용자가 명시하면 그 범위.
- 민감 정보(HR, 급여)는 제외.

## Length
- 우선순위 5개. 각 항목 한 줄.
- 전체 ≤ 800자.

## Format
```markdown
## 오늘 우선순위 (YYYY-MM-DD)

1. **[severity] [출처]** <한 줄 요약> — <왜 오늘 해야 하나>
2. **[severity] [출처]** ...
3. **[severity] [출처]** ...
4. **[severity] [출처]** ...
5. **[severity] [출처]** ...

## 보류 / 위임 후보
- ...
- ...

## 신호 통계
- Slack 멘션: N / Linear 이슈 변경: N / GitHub PR: N / 미팅: N
```

severity = **high / mid / low** (시간 민감도 × 영향도).

## Examples

<example>
<good>
1. **[high] [Linear]** AUTH-241 prod 버그 — eng 가 fix 푸시했고 머지 승인 대기. PM 검수 30분.
2. **[high] [Slack]** CFO 가 11AM 까지 Q3 OKR 초안 요청 (DM, #leadership).
3. **[mid] [GitHub]** PR #88 PRD 변경 review 요청 — 2일 묵음.
</good>
<bad>
1. 슬랙 메시지가 많이 있습니다.
2. 여러 가지 이슈가 진행 중입니다.
</bad>
</example>
