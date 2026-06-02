# /retro — 폐루프 트랜스크립트 회고

## Task

최근 N일의 Claude Code 트랜스크립트에서 **자주 고치는 항목 / 반복 지시 / 동일 실수** 를 찾아내, 어디(CLAUDE.md / 스킬 / 슬래시) 에 흡수할지의 결정안과 PR 초안을 출력한다.

## Scope

- 분석만 한다. 실제 CLAUDE.md / 스킬 파일을 직접 수정하지 않는다 (PR 초안만 제시).
- 입력: `~/.claude/projects/<hash>/*.jsonl` 또는 사용자가 지정한 경로.
- 기본 기간 7일. 사용자가 `--since YYYY-MM-DD` 명시하면 그 범위.

## Length

- 패턴 3–10개. 전체 1,500–3,000자.

## Format

```markdown
## 분석 범위
- 기간: YYYY-MM-DD ~ YYYY-MM-DD
- 세션 수: N / 총 턴 수: M

## 시그널 패턴 (빈도순)
1. **[N회] 패턴**: <한 줄 설명>
   - 예시 인용: > "..."
   - > "..."
   - 흡수처: ~/.claude/CLAUDE.md / 레포 CLAUDE.md / 스킬 / 슬래시 / 스팸 (흡수 안 함)
   - 제안 패치:
     ```diff
     + <한 줄>
     ```
2. ...

## 결정 표
| 패턴 | 빈도 | 흡수처 | 제안 |
|---|---|---|---|

## 룰 정원 점검 (분기 1회 권장)
- 중복 룰 후보: <파일> + <파일> 의 "X" — 한 곳으로 합치기 제안.
- 6개월 미사용 스킬 후보: <목록>

## PR 초안
```

title: chore(retro): WW <NN> 2026 absorb <N> rules
body:

- ~/.claude/CLAUDE.md: + "<patch>"
- skills/polish.md: + <patch>
- 스팸으로 처리: <패턴>

```
```

## Examples

<example>
<good>
1. **[7회] 보고서 톤이 너무 캐주얼**
   - "더 formal 하게" 요청 7회 / 7일
   - 흡수처: ~/.claude/CLAUDE.md (전역 톤)
   - 제안 패치: `+ 공식 보고서 작성 시 ToS 는 formal·존댓말 기본.`
</good>
<bad>
1. 사용자가 보고서 톤을 자주 고친다 → CLAUDE.md 어딘가에 넣어야 할 듯.
</bad>
</example>

<example>
<good>
3. **[12회] "PR 머지 전 테스트 돌려" 매번 요청**
   - 흡수처: PostToolUse hook (이미 존재) — 강화 불필요. 단, CLAUDE.md 에 "변경 후 사다리 1단 강제" 한 줄 추가 권장.
</good>
<bad>
3. 테스트를 자주 까먹는다 → 새 스킬 만들자.  (이미 hook 으로 처리 가능한데 중복 생성)
</bad>
</example>
