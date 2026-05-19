# SoT 정책 — Notion ↔ GitHub

> 본 가이드는 Notion과 GitHub를 동시에 쓴다. 어느 쪽이 진실인지(Source of Truth)를 명시하지 않으면 콘텐츠가 분산되고 동기화 비용이 폭발한다. 이 문서가 규칙이다.

---

## 1. SoT = 어떤 도구가 "정본"인가

| 자료 유형 | SoT | 비고 |
|---|---|---|
| 가이드 챕터 본문 | **GitHub** | 모든 본문은 본 레포 `.md` 가 정본 |
| 슬래시 커맨드 / 스킬 / 에이전트 | **GitHub** | `templates/`, `skills/`, `.claude/agents/` |
| 결정 (PRD / RFC) | **GitHub Issues** | `.github/ISSUE_TEMPLATE/` 로 제출 |
| 변경 이력 | **GitHub** | `CHANGELOG.md` |
| 자료 조사·인터뷰 원본 | **Notion** | raw 그대로 |
| 실험 로그 / 데이터셋 | **Notion** | A/B 결과 노트, 메모 |
| 일정 / 회의록 | **Notion** | |
| 외부 공유 (제휴·강의용) | **Notion** | 필요 시 GitHub 본문을 Notion에 인용 |

## 2. 동기화 방향 — Promotion

```
Notion (raw, 탐색)  ──promote──▶  GitHub (정제, 정본)
        ▲                                 │
        └────── 인용·링크만 역방향 ───────┘
```

- **Promotion 규칙**: Notion 노트에서 결론이 나오면 → GitHub Issue/PR 로 옮긴다.
- Notion 페이지 상단에 `[Promoted to GH #123]` 한 줄을 박는다 (자동화 또는 수동).
- 역방향(GitHub → Notion)은 **인용·링크만** 허용. 본문을 Notion에 복제하지 않는다.

## 3. 자동화 트리거

- `n8n` 워크플로우 (챕터 3.5):
  - Notion 페이지에 `promote-to-gh` 태그 → GitHub Issue 자동 생성
  - GitHub Issue 닫힘 → Notion 페이지에 `[Closed: #issue]` 자동 표기
- Claude Code MCP (챕터 3.1):
  - 작업 시작 시 `INDEX.md` → Notion 관련 페이지를 한 번에 호출
  - 작업 종료 시 변경 요약을 Notion 데일리 로그에 append

## 4. 안티패턴

- 같은 PRD가 Notion에도 있고 GitHub Issue에도 있다 → **하나만 정본**
- 챕터 본문을 Notion에서 편집한다 → 금지. GitHub PR로만.
- 인터뷰 quote를 GitHub Issue에 통째 붙여넣는다 → Notion 링크 + 핵심 인용 3줄까지.

## 5. 체크리스트 — 새 자료를 만들 때

- [ ] 이 자료의 SoT 는 어디인가?
- [ ] 다른 도구에는 어떤 형태로 인용되는가? (링크 / 메타데이터 / 인용)
- [ ] Promotion 규칙을 따랐는가?
- [ ] INDEX.md 에 외부 SoT 도 등재했는가?

---

last_updated: 2026-05-19
참고 챕터: 3.1 (MCP) · 3.5 (n8n 자동화)
