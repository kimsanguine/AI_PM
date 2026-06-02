# /review — 검증 사다리 기반 review

## Task

지정된 PR / 챕터 / 문서를 **검증 사다리 4단계** 순서로 review 하고, 발견 사항을 severity 별로 보고한다.

## Scope

- review 만 한다. 직접 수정은 하지 않는다 (제안 패치만 코드 블록으로).
- 본 가이드 `CLAUDE.md` 의 룰을 기준으로 한다.
- 1단·2단 자동 통과 가능하면 모델이 도구로 검증 (Bash 등).

## Length

- 발견 사항 severity 별 정렬. 단순 nit 은 묶어서 한 절.
- 전체 1,000–2,500자.

## Format

```markdown
## 검증 사다리
- [x/✗] 1단 자동 포맷
- [x/✗] 2단 링크·테스트
- [x/✗] 3단 시각 렌더
- [x/✗] 4단 LLM 룰 적합성 (이 review)

## 발견 (severity 별)
### high
- L42: <인용 한 줄>
  - 문제: <한 줄>
  - 제안: `<패치>`

### mid
- L88: ...

### low / nit
- L120 / L155 / L201 (묶음): ...

## 통과 항목
- 모델 ID 일치 / 4섹션 포맷 / 톤 일관

## 권고
머지 / 수정 후 머지 / 거절 — 한 줄 사유.
```

## Examples

<example>
<good>
### high
- L42: "Claude 4 Opus" 사용
  - 문제: 마케팅 이름 금지(CLAUDE.md 룰).
  - 제안: `claude-opus-4-8`
</good>
<bad>
전반적으로 좋아 보이고 머지해도 될 듯합니다.
</bad>
</example>
