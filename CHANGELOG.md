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

### Planned (v1.2 / v1.3)
- 폴더 재편 (`docs/partN/...`) — 36개 cross-link 일괄 수정 PR.
- 신규 챕터: **3.2.1 패턴 카탈로그** · **3.6 Claude Code on the web**.
- 기존 챕터 35개에 front-matter 일괄 추가.
- Part 1~3 4.7 기준 재검수 (모드/effort, adaptive thinking, subagent fan-out).

---

## [v1.0] — 2026-04 (기존)

### Added
- Part 1–8 본문 + Appendix A.1–A.10
- `templates/commands/today.md`, `prd.md`, `status.md`
- `skills/prd-generator/`
- `samples/` 3종
