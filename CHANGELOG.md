# Changelog

본 가이드의 변경 이력. [Keep a Changelog](https://keepachangelog.com/) 형식.

---

## [v1.7.0] — 2026-06-03

### Added

- `docs/part2-basics/2.4-custom-subagents.md` — `/agents` 명령어 대화형 에이전트 생성(Installed·Create UI), 파일 직접 작성 4섹션 템플릿, `@에이전트명` 호출 방법, PM 필수 3종 에이전트 표, `/agents/<이름>` 형식 오용 경고 추가.
- `docs/part2-basics/2.3-project-memory.md` — Claude MD Management 공식 플러그인 상세 소개: `/revise-claude-md`·`claude-md-improver` 스킬·5단계 워크플로우·6가지 품질 기준·GitHub 링크 포함.
- `docs/part3-advanced/3.2-claude-md-deep-dive.md` — 실전 전역 CLAUDE.md 예시: 운영 중인 9개 룰 전문 공개(Think Before Coding·Simplicity First·Surgical Changes·Goal-Driven·모델 판단 작업에만·Tests verify intent·Checkpoint·Fail loud·에이전트 Scope) + 설계 원칙 해설.
- `docs/part3-advanced/3.1-mcp-integration.md` — 바이브코딩 필수 MCP & 플랫폼 8종 소개: Supabase·Vercel·Netlify·Cloudflare·Railway·Render·context7·GitHub·Insforge, 권장 설치 순서.
- `docs/part6-delivery/6.1-delivery-vibe-coding.md` — 이미지·시각자료 활용(드래그앤드롭·Ctrl+Y·@참조), 빠른 디자인 이터레이션(ASCII 목업·Mermaid 차트), Vercel 배포(MCP 연결·수동 명령어·장점) 추가.
- `docs/part2-basics/2.7-hooks.md` — Hook으로 QA 자동화: PostToolUse+Stop Hook 자동 테스트·린트, QA 목표 지정 프롬프트, 테스트 계획→병렬 서브에이전트 분배 2단계, E2E Playwright 폴더 구조, 엣지 케이스 요청 패턴.
- `docs/appendix/A.11-prompt-cheatsheet.md` — CoT 프롬프팅(단순 요청 vs CoT 비교표·트리거 표현), `<thinking>`/`<answer>` 태그 분리 패턴(요청 방법·XML 출력 예시·사용 상황), SPEC.md 기획서(기술스택·ADR·아키텍처·디자인 구성) 추가.
- `docs/appendix/A.12-faq-troubleshooting.md` — 필수 단축키 5종(ESC·ESC+ESC·Shift+Enter·Shift+Tab·Tab) + 경로 자동완성, `-c`/`-r` CLI 플래그 비교, Explanatory Output 설명형 출력 설정 방법·초급자 중요성·비교표·`/config` 권장 옵션 4가지 추가.

---

## [v1.6.0] — 2026-06-03

### Added

- 신규 챕터 `docs/part3-advanced/3.8-ralph-loop-automation.md` — `--max-iterations + --completion-promise` 플래그로 조건 달성까지 자율 반복하는 PM 리서치 자동화 (경쟁사 리스트업·리드 수집 실전 예시).
- 신규 챕터 `docs/part6-delivery/6.2-agent-product-ui.md` — 에이전트 제품 PM UI 판단 원칙: Non-negotiable 4원칙(투명성·사용자 제어·선제 피드백·에러 복구), Agent 특화 KPI(Task Completion Rate·Autonomy Trust Score), Autonomy-Trust Matrix.
- `docs/part3-advanced/3.5-automation-n8n.md` — Claude 생태계 3-레이어 아키텍처 섹션: Claude.ai(전략 대화)·Claude Code(파일 실행)·n8n(스케줄 배경 자동화) 역할 경계와 L1~L4 단계적 도입 로드맵 추가.
- `docs/part5-definition/5.1-definition-write-prd.md` — PRD-in-Repo 패턴(Living Document 루프) 및 Super MVP 3단계 프로토타이핑(ChatGPT 원형→Claude Code 구현→3모델 A/B 비교) 섹션 추가.
- `docs/part2-basics/2.5-agent-teams.md` — Boris Cherny(Claude Code 제작자)의 병렬 세션 12-tip 체크리스트: 로컬 5+웹 10=15개 동시 세션, "덜 똑똑한 모델 반복 > Opus 1-shot" 역설 원칙, Sub-agent 전문화 패턴 추가.
- `docs/part3-advanced/3.2-claude-md-deep-dive.md` — 8-layer 컨텍스트 모델 전체 그림(`/memory` 시각화 팁 포함), Lazy Loading(`@파일` 참조 분리, 토큰 80% 절감), 팀 Git 자동 업데이트 루프·AGENTS.md 멀티툴 호환 트릭·분기별 리뷰 체크리스트 추가.
- `docs/part2-basics/2.2-modes-and-depth.md` — Plan Mode 실전 수치(토큰 30~50% 절감 이유, "수정 3번=토큰 3배" 비교) 및 7일 토큰 예산 운영 패턴(모델 역할 분리표) 추가.
- `docs/part3-advanced/3.4-custom-skills.md` — 재사용 메커니즘 컨텍스트 비용 비교 매트릭스(CLAUDE.md·스킬·MCP·Sub-Agent) 및 WAT 프레임워크(Workflows+Agents+Tools, Tool Atomicity 원칙) 추가.
- `docs/part2-basics/2.3-project-memory.md` — CLAUDE.md 점진적 구축 원칙("같은 내용 두 번이면 분리"), 다이어트 사이클(300줄→80줄, 토큰 4000→800), AGENTS.md 멀티툴 호환 트릭 추가.

---

## [v1.5.0] — 2026-06-02

### Fixed

- `docs/part2-basics/2.2-modes-and-depth.md` — thinking 키워드 교정: `think`/`think harder`는 일반 텍스트로 전달되며 `ultrathink`만이 deep reasoning 키워드로 인식됨(공식 확정). adaptive reasoning 설명 교정: Opus 4.7+ 에서 항상 on이며 끄는 것이 불가능함.
- `docs/part6-delivery/6.1-delivery-vibe-coding.md` — MCP 설정 현행화: `settings.json mcpServers` 블록 → `claude mcp add` CLI / `.mcp.json` 방식으로 교정.
- `docs/appendix/A.1-running-scenario.md` — 서브에이전트 호출 문법 교정: `/agents/<이름>` → `@<agent-name>` 형식으로 교정.
- `docs/part2-basics/2.7-hooks.md` — 훅 이벤트 수 정정: "30종" → 8가지(PreToolUse·PostToolUse·Notification·Stop·SubagentStop·PreCompact·SessionStart·SessionEnd).
- `docs/part8-strategy/8.2-growth-path.md` — 레거시 링크 교정: `docs.anthropic.com` → `platform.claude.com/docs`.

### Added

- `docs/part3-advanced/3.7-plugins-and-marketplace.md` — 외부 플러그인 보안 체크 4단계 및 AI_PM vs knowledge-work-plugins 생태계 포지셔닝 표.
- `docs/part3-advanced/3.4-custom-skills.md` — 스킬 자동 발동 실패 진단 5단계 절 추가.
- `docs/part3-advanced/3.1-mcp-integration.md` — MCP 설치 후 연동 확인 체크리스트 추가.
- `docs/appendix/A.12-faq-troubleshooting.md` — Quickstart 2-트랙화(데스크톱/IDE 무터미널 + CLI), 외부 스킬 보안 FAQ, 스킬 자동 발동 실패 FAQ, MCP 연동 검증 FAQ, 토큰 비용 관리 FAQ 추가.
- `docs/part1-foundations/1.3-install-and-first-run.md` — 터미널 없이 시작하기(데스크톱 앱/IDE) 트랙 추가.
- `docs/part2-basics/2.6-human-in-the-loop.md` — Claude 응답 신뢰 수준 3-tier 표(완료/시도/불확실) 추가.
- `docs/part1-foundations/1.2-what-is-claude-code.md` — 일반 챗봇 vs Claude Code 기능 비교표 추가.
- `docs/part6-delivery/6.1-delivery-vibe-coding.md` — "처음엔 작게 시작하세요" 진입 조언 추가.
- `README.md` — `knowledge-work-plugins` 생태계 포지셔닝 언급 추가.

---

## [v1.4.0] — 2026-06-02

### Added

- 신규 챕터 `docs/part2-basics/2.0-toolkit-map.md` — Claude Code 도구 5범주 지도(기억·스킬·자동 실행·대리인·확장), Part 2 입문 overview.
- 신규 챕터 `docs/part3-advanced/3.7-plugins-and-marketplace.md` — 명령·스킬·에이전트·훅·MCP를 한 묶음으로 포장·공유하는 플러그인 + 마켓플레이스 2단계 설치.
- 신규 챕터 `docs/appendix/A.11-prompt-cheatsheet.md` — 본문 핵심 프롬프트 1페이지 치트시트(바로 복사해 쓰는 1~2줄 모음).
- 신규 챕터 `docs/appendix/A.12-faq-troubleshooting.md` — 비개발자 PM 첫 30분 Quickstart + 증상→원인→해결 FAQ·트러블슈팅 허브.
- 비개발자 온램프 보강 — 데스크톱앱/IDE 진입, 30초 검증 루틴, 입력 비교 실습, 발동조건 판별표, auto memory 절.
- 프레임워크 스킬 3종 — `jtbd`(JTBD, Clayton Christensen / Anthony Ulwick), `opportunity-solution-tree`(OST, Teresa Torres), `working-backwards`(PR-FAQ, Amazon).
- `templates/commands/pm-setup.md` — `/pm-setup` 대화형 PM 컨텍스트 부트스트랩(CLAUDE.md 8축 + INDEX.md 초안 자동 작성).
- 인터랙티브 코스 — `templates/commands/start.md` · `start-1.md` · `start-2.md` · `start-3.md`(`/start`~`/start-3` 레벨별 손으로 따라 하는 온보딩).
- `.claude-plugin/marketplace.json` — `ai-pm` 플러그인 (`/plugin marketplace add kimsanguine/AI_PM` → `/plugin install ai-pm@ai-pm`).

### Changed

- 자산 카운트 일괄 갱신 — 슬래시 9 → 14, 스킬 5 → 8, 플러그인 1종 신규(README 구조 박스 · `CLAUDE.md` 자산 현황 · `INDEX.md` 목록).
- README — 버전 배지 `guide-v1.3` → `guide-v1.4`, Part 2 표에 2.0 · Part 3 표에 3.7 · Appendix 표에 A.11/A.12 행 추가, "빠른 시작"에 인터랙티브 코스/플러그인 설치 두 진입로, 이론 프레임워크 표에 JTBD · OST · Working Backwards 추가.
- `CLAUDE.md` 푸터 `guide_version` v1.3 → v1.4.

### Fixed

- hooks `settings.json` 3중 중첩 스키마 교정.
- MCP 설정을 `claude mcp add` / `.mcp.json` / 원격 OAuth 기준으로 현행화.
- `#` 메모리를 영구 auto memory 로 정정.
- 설치 경로(native installer · `| bash` · 플랜 · 브라우저 로그인) · `claude doctor` · 모델명 현행화.
- effort 순서/기본값(high) 정정.
- 슬래시 ↔ 스킬 병합 반영.
- 2.5 에이전트 팀 현행화 — Dynamic Workflows 공존.
- `claude agents list` → `/agents` 로 교정.

---

## [v1.3.0] — 2026-06-02

### Added

- `LICENSE` — Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) legal code 전문. README 배지와 일치.
- `.lycheeignore` — `linear://` 스킴 무시 항목 추가.

### Changed

- 모델 베이스라인 일괄 갱신: `claude-opus-4-7` → `claude-opus-4-8` (front-matter · 배지 · agent/skill `model` 필드 · 사양표).
- 챕터 `3.2.2` 를 4.8 로 retarget — 리서치로 4.7 의 literal-following 행동 특성(literal following · adaptive-thinking-only · fewer-subagents · effort 존중)이 4.8 에 동일 적용됨을 공식 문서로 확인. 파일명은 URL 안정을 위해 유지하고 "4.8 에서 더해진 것"(effort 기본 high · Dynamic Workflows · mid-conversation system messages · 정직성 개선) 절을 추가. 4.6→4.7 마이그레이션 절과 과거 CHANGELOG 이력만 historical 로 유지.
- `.markdownlint.json` 규칙 완화 — MD014 `false`, MD025 `front_matter_title`, MD029 `false`.

### Fixed

- markdownlint CI 그린화 — 전역 `markdownlint-cli2 --fix` 로 공백 정리 약 1,230건. 잔여로 `competitor.md` 표와 `CLAUDE-md-starter.md` 헤딩을 수동 수정.
- lychee 링크 CI 그린화 — docs/ 재편으로 stale 해진 상대링크 6건을 `docs/partN/` 경로로 교정.

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

## [v1.2.1] — 2026-05-19

### Added

- 레포 배너 이미지 추가.
- companion 레포 `ai-prompts-playbook` 링크 추가.

### Changed

- README — "Claude Code for PMs" 리드로 재포지셔닝.

### Fixed

- CI 워크플로 수정 — encoding-sanity self-match 수정, markdownlint 완화.

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
