# Changelog

본 가이드의 변경 이력. [Keep a Changelog](https://keepachangelog.com/) 형식.

---

## [v1.1] — 2026-05-19 (P0: Dogfood)

### Added
- 루트 `CLAUDE.md` — 본 레포의 dogfood. 8축 프레임워크 (Project / Conventions / Workflows / Tools / Voice / Examples / Escalation / Knowledge-Map).
- 루트 `INDEX.md` — 주석 달린 지식 지도 (경로 · 소유자 · 용도 · 신선도).
- `.github/` — ISSUE_TEMPLATE (PRD / Discovery / RFC / UseCase / Bug), PR 템플릿, `labels.yml`, `CODEOWNERS`.
- 관련 프로젝트에 `kimsanguine/hplan` 추가.
- `docs/operations/sot-policy.md` — Notion ↔ GitHub SoT 정책 + Promotion 규칙.
- `docs/operations/closed-loop.md` — `/retro` 주 1회 운영, One rule = one place.
- `templates/claude-home/` — 전역 `~/.claude/` 스타터 (CLAUDE.md + guides 3종 + skills `polish`).

### Changed
- README — `claude-opus-4-7` 기준 배지 + 부제 추가, "컨텍스트 인프라 4요소" 박스로 인트로 교체, "권장 시작 트랙(레벨별)" 표로 교체, 프로젝트 구조 박스 갱신, 빠른 시작에 `INDEX.md` / `CLAUDE.md` 진입점 추가.
- README 인코딩 깨짐 일괄 수정 (`ǭ�지`, `보여:니다`, `Part 18`, `방법론,��니다`, `학슰`, `(중급))`, `기벘`).
- 관련 프로젝트의 단계 라벨을 상단 학습 경로(AI_Human → AI_Engineer → AI_PM)와 정합화.

### Removed
- **`260317_community_manager/`, `260317_seo_optimizer/`, `260317_voice_clone_studio/`** — 가이드 본문에서 직접 참조되지 않는 별도 Python 프로젝트 3종 제거. 본 레포의 정체성은 "PM playbook" 이므로, 챕터와 결합되지 않은 독립 스캐폴딩은 dead weight 로 판단.
- **`EXAMPLES.md`** — `260317_*` 매핑 표였으므로 동반 제거.

### Added (v1.1 후속)
- 신규 챕터 `2.7-hooks.md` — SessionStart / PostToolUse / Stop 훅, 검증 사다리와의 매핑.
- 신규 챕터 `3.2.2-claude-md-for-4-7.md` — 4.7 literal following 대응 8축 프레임워크, 마이그레이션 체크리스트 (본 라운드의 헤드라인 챕터).
- `.claude/agents/` — engineering-reviewer · exec-advisor · user-researcher.
- `templates/hooks/` — stop-notify.sh · posttooluse-fmt.sh · sessionstart-load.sh.
- `templates/commands/` 신규 6종 — discovery · competitor · briefing · review · postmortem · retro.
- `skills/` 신규 4종 — discovery-synthesizer · competitor-battlecard · experiment-analyzer · kpi-card-builder (각 SKILL.md + good/bad 예시).
- `.github/workflows/` — lint.yml (markdownlint + 인코딩 detector), links.yml (lychee), frontmatter.yml.
- `.github/scripts/validate_frontmatter.py` — front-matter 스키마 검증.

---

## [v1.2] — 2026-05-19 (Structure & Content)

### Added
- 신규 챕터 `docs/part3-advanced/3.2.1-claude-md-patterns.md` — mono / multi-folder / layered 패턴 카탈로그, 5문항 선택 가이드, 안티패턴.
- 신규 챕터 `docs/part3-advanced/3.6-claude-code-on-the-web.md` — 4가지 실행 표면(CLI / Web·Mobile / GitHub Action / Cloud worktree), 네트워크 정책 3모드, 검증 사다리 3단의 자동화 가능성.
- 기존 챕터 36개에 YAML front-matter 일괄 추가 (chapter / title / claude_model / last_updated) — CI frontmatter validator 가 실제 강제 가능한 상태.

### Changed
- **폴더 재편**: 38개 챕터를 flat 루트 → `docs/partN-*/` 폴더 구조로 이동. git mv 로 history 보존 (similarity 97-100%).
  - 자동 링크 갱신: 138 markdown link + 38 INDEX.md 백틱 경로 일괄 재계산 (`/tmp/migrate_to_docs.py`).
- `docs/part1-foundations/1.2-what-is-claude-code.md` — 본 가이드의 기준 모델 사양 표 추가 (1M context, Files API, prompt caching, adaptive thinking, 고해상도 이미지).
- `docs/part2-basics/2.2-modes-and-depth.md` — **4.7 변경 반영 가장 큰 챕터**. extended thinking budget 제거 명시, effort + adaptive thinking 2축 모델 신규 절(2.0), 4.6→4.7 syntax 매핑, 요점 정리 표 확장.
- `docs/part2-basics/2.4-custom-subagents.md` — 4.7 의 fewer-subagents-by-default 행동, fan-out 트리거 명시 요구.
- `docs/part2-basics/2.5-agent-teams.md` — 사용자 측 3–6 병렬 세션 운영 패턴, Cloud worktree(3.6) 와 Stop 훅(2.7) 연결.
- `docs/part3-advanced/3.2-claude-md-deep-dive.md` — 3.2 / 3.2.1 / 3.2.2 시리즈의 위치 callout, 루트 `/CLAUDE.md` worked example 링크.
- 루트 `CLAUDE.md` — 자산 현황(슬래시 9 · 스킬 5 · 에이전트 3 · 훅 3) 명시, Hooks 항목 추가, Knowledge Map 갱신, `/retro` 가 실제 자산임을 반영.
- README — Part 3 표에 3.2.1 / 3.6 행 추가.
- INDEX.md — 신규 챕터 2종 등재.

### Migration notes
- 이전 `(./X.X-name.md)` 링크들은 모두 `(./docs/partN/X.X-name.md)` 또는 part-relative 경로로 갱신됨. 외부 북마크가 있다면 갱신 필요.

---

## [v1.0] — 2026-04 (기존)

### Added
- Part 1–8 본문 + Appendix A.1–A.10
- `templates/commands/today.md`, `prd.md`, `status.md`
- `skills/prd-generator/`
- `samples/` 3종
