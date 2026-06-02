# INDEX.md — 지식 지도

> 본 레포에서 무엇이 어디에 있는지의 진입점.
> Claude Code는 작업 전 이 파일을 먼저 읽고 관련 파일만 펼친다.
>
> 형식: `경로` · owner · use · freshness

---

## 운영 (Root)

- `README.md` — owner: @kimsanguine — use: 첫 진입점, 학습 동선 — freshness: 2026-05
- `CLAUDE.md` — owner: @kimsanguine — use: Claude Code 행동 규칙 (8축) — freshness: 2026-05
- `INDEX.md` (본 파일) — owner: @kimsanguine — use: 지식 지도 — freshness: 2026-05
- `CHANGELOG.md` — owner: @kimsanguine — use: 버전 이력 — freshness: 2026-05
- `00-index.md` — owner: @kimsanguine — use: 챕터 목차(상세) — freshness: 2026-05

## Part 1 — Foundations

- `docs/part1-foundations/1.1-why-now.md` — use: AI 네이티브 PM의 명제
- `docs/part1-foundations/1.2-what-is-claude-code.md` — use: Claude Code 정의·비교
- `docs/part1-foundations/1.3-install-and-first-run.md` — use: 설치 + 첫 실행

## Part 2 — Basics

- `docs/part2-basics/2.0-toolkit-map.md` — use: 도구 5범주 지도 (기억·스킬·자동 실행·대리인·확장) 입문 overview
- `docs/part2-basics/2.1-files-and-input.md` — use: 파일/이미지 입력, XML 태그 패턴
- `docs/part2-basics/2.2-modes-and-depth.md` — use: effort · adaptive thinking
- `docs/part2-basics/2.3-project-memory.md` — use: 메모리 계층 (global ↔ repo)
- `docs/part2-basics/2.4-custom-subagents.md` — use: 서브에이전트 정의
- `docs/part2-basics/2.5-agent-teams.md` — use: 멀티에이전트 + 병렬 세션
- `docs/part2-basics/2.6-human-in-the-loop.md` — use: HITL · 검증 사다리
- `docs/part2-basics/2.7-hooks.md` — use: SessionStart / PostToolUse / Stop 훅 (폐루프 자동화)

## Part 3 — Advanced

- `docs/part3-advanced/3.1-mcp-integration.md` — use: Notion / Linear / Slack / GitHub MCP
- `docs/part3-advanced/3.2-claude-md-deep-dive.md` — use: CLAUDE.md 8축 프레임워크
- `docs/part3-advanced/3.2.1-claude-md-patterns.md` — use: 패턴 카탈로그 (mono / multi-folder / layered)
- `docs/part3-advanced/3.2.2-claude-md-for-4-7.md` — use: 4.7 시대 CLAUDE.md (literal following, 마이그레이션)
- `docs/part3-advanced/3.3-slash-commands.md` — use: 슬래시 커맨드 (4섹션 표준)
- `docs/part3-advanced/3.4-custom-skills.md` — use: SKILL.md 패키지
- `docs/part3-advanced/3.5-automation-n8n.md` — use: 외부 자동화
- `docs/part3-advanced/3.6-claude-code-on-the-web.md` — use: 웹·모바일·GitHub Action 실행 환경
- `docs/part3-advanced/3.7-plugins-and-marketplace.md` — use: 플러그인 묶음 배포 + 마켓플레이스 2단계 설치

## Part 4 — Discovery

- `docs/part4-discovery/4.1-discovery-user-research.md`
- `docs/part4-discovery/4.2-discovery-competitive-analysis.md`

## Part 5 — Definition

- `docs/part5-definition/5.1-definition-write-prd.md`
- `docs/part5-definition/5.2-definition-product-strategy.md`

## Part 6 — Delivery

- `docs/part6-delivery/6.1-delivery-vibe-coding.md`
- `docs/part6-delivery/6.2-delivery-visual-assets.md`
- `docs/part6-delivery/6.3-delivery-github-deploy.md`

## Part 7 — Growth

- `docs/part7-growth/7.1-growth-experiment-analysis.md`
- `docs/part7-growth/7.2-growth-kpi-dashboard.md`
- `docs/part7-growth/7.3-ai-observability.md`

## Part 8 — Strategy

- `docs/part8-strategy/8.1-ai-product-strategy.md`
- `docs/part8-strategy/8.2-growth-path.md`

## Appendix

- `docs/appendix/A.1-running-scenario.md` — use: Discovery → Delivery → Growth 전체 흐름
- `docs/appendix/A.2-level3-exercises.md`
- `docs/appendix/A.3-usecase-scenarios.md`
- `docs/appendix/A.4-usecase-daily-briefing.md`
- `docs/appendix/A.5-usecase-status-report.md`
- `docs/appendix/A.6-usecase-battle-cards.md`
- `docs/appendix/A.7-usecase-customer-personas.md`
- `docs/appendix/A.8-usecase-investment-memo.md`
- `docs/appendix/A.9-usecase-process-flowchart.md`
- `docs/appendix/A.10-usecase-content-adaptation.md`
- `docs/appendix/A.11-prompt-cheatsheet.md` — use: 핵심 프롬프트 1페이지 치트시트
- `docs/appendix/A.12-faq-troubleshooting.md` — use: 첫 30분 Quickstart + FAQ·트러블슈팅 허브

## 자산

### 슬래시 커맨드 (`templates/commands/`)

- `today.md` — `/today` 일일 브리핑 (기존)
- `prd.md` — `/prd` PRD 생성 (기존)
- `status.md` — `/status` 상태 보고서 (기존)
- `discovery.md` — `/discovery` 인터뷰·설문 합성
- `competitor.md` — `/competitor` 경쟁사 배틀카드
- `briefing.md` — `/briefing` 크로스 툴 일일 우선순위
- `review.md` — `/review` 검증 사다리 4단계 review
- `postmortem.md` — `/postmortem` blameless 사후 분석
- `retro.md` — `/retro` 트랜스크립트 폐루프 회고
- `pm-setup.md` — `/pm-setup` 대화형 PM 컨텍스트 부트스트랩 (CLAUDE.md + INDEX.md 초안)
- `start.md` — `/start` 인터랙티브 온보딩 코스 인덱스
- `start-1.md` — `/start-1` 입문 트랙 (Part 1~2)
- `start-2.md` — `/start-2` 활용 트랙 (Part 2~3)
- `start-3.md` — `/start-3` 워크플로 관통 트랙 (Part 4~6)

### 스킬 (`skills/`)

- `prd-generator/SKILL.md` (기존)
- `discovery-synthesizer/SKILL.md` — 인사이트 합성
- `competitor-battlecard/SKILL.md` — 경쟁사 카드
- `experiment-analyzer/SKILL.md` — A/B 결과 분석
- `kpi-card-builder/SKILL.md` — KPI 정의 카드
- `jtbd/SKILL.md` — Jobs to be Done job statement 재구성
- `opportunity-solution-tree/SKILL.md` — outcome → opportunity → solution → experiment 트리
- `working-backwards/SKILL.md` — PR-FAQ 역방향 기획

### 서브에이전트 (`.claude/agents/`)

- `engineering-reviewer.md` — 엔지니어 관점 PR/코드 review
- `exec-advisor.md` — 임원 관점 PRD/전략 review
- `user-researcher.md` — UX 리서치 합성

### 전역 스타터 (`templates/claude-home/`)

- `CLAUDE.md` — `~/.claude/CLAUDE.md` 스타터
- `guides/writing.md` · `review.md` · `evals.md` (lazy load)
- `skills/polish.md` — `/polish` 글 다듬기

### Hooks (`templates/hooks/`)

- `stop-notify.sh` — 세션 종료 알림
- `posttooluse-fmt.sh` — 편집 직후 포매터
- `sessionstart-load.sh` — 세션 시작 시 INDEX.md 주입

### 운영 (`docs/operations/`)

- `sot-policy.md` — Notion ↔ GitHub SoT
- `closed-loop.md` — `/retro` 운영, One rule = one place

### 플러그인 (`.claude-plugin/`)

- `marketplace.json` — `ai-pm` 마켓플레이스/플러그인 정의 (`/plugin marketplace add kimsanguine/AI_PM` → `/plugin install ai-pm@ai-pm`)

### 기타

- `templates/CLAUDE-md-starter.md` — 새 프로젝트용 CLAUDE.md 스타터

## 샘플 데이터

- `samples/ab-test-results.csv` — use: 7.1 A/B 분석 실습
- `samples/competitor-data.json` — use: 4.2 경쟁사 분석 실습
- `samples/user-survey-results.csv` — use: 4.1 유저 리서치 실습

## .github (메타)

- `.github/ISSUE_TEMPLATE/` — PRD / Discovery / RFC / UseCase / Bug
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/labels.yml`
- `.github/CODEOWNERS`

## 외부 (참조)

- **Notion** — 자료 조사·인터뷰 원본·실험 로그 (SoT, 정책은 향후 명문화)
- **kimsanguine/hplan** — Product Build Gate (자매 PM 도구)
- **kimsanguine/AI_Human** — AI 입문 100일 (시리즈 1단계)
- **kimsanguine/AI_Engineer** — AI Agent 100개 직접 구현 (시리즈 2단계)
- **kimsanguine/ai-prompts-playbook** — 3-Layer 인지 프레임워크 (참조)

---

last_updated: 2026-06-02
