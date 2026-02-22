# AI 네이티브 PM을 위한 Claude Code 실전 가이드

> **"도구를 배우는 것이 아니라, PM의 일하는 방식을 재설계한다."**

---

## 이 가이드에 대하여

이 가이드는 Claude Code라는 CLI 기반 AI 에이전트를 활용하여, PM이 Discovery → Definition → Delivery → Growth의 전체 제품 개발 사이클에서 어떻게 일하는 방식을 변화시킬 수 있는지를 다룹니다.

단순한 도구 사용법이 아닌, **실제 터미널 입력 → Claude 응답 → PM 판단**의 워크스루를 통해 학습합니다.

### 대상 독자

| 레벨 | 설명 | 권장 경로 |
| --- | --- | --- |
| **J (Junior)** | PM 경력 0~2년, AI 도구 경험 적음 | Part 1 → 2 → 4 순서대로 |
| **P (Practitioner)** | PM 경력 3~7년, AI 도구 일부 사용 중 | Part 1 훑고 → Part 3~6 집중 |
| **L (Lead)** | PM 경력 7년+, 팀/조직 리딩 | Part 1 훑고 → Part 5~8 집중 |

---

## 목차

### Part 1: 시작하기 — 왜 지금, AI 네이티브 PM인가

PM의 역할이 어떻게 변하고 있는지, 왜 Claude Code인지, 그리고 첫 설치까지.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 1.1 | [1.1-why-now.md](./1.1-why-now.md) | PM 역할 변화, Before/After 시간 배분, 코스 구조 | 모든 레벨 |
| 1.2 | [1.2-what-is-claude-code.md](./1.2-what-is-claude-code.md) | ChatGPT/Copilot과의 차이, CLI의 4가지 장점 | 모든 레벨 |
| 1.3 | [1.3-install-and-first-run.md](./1.3-install-and-first-run.md) | 설치 가이드, 첫 대화 예시, 트러블슈팅 | J |

---

### Part 2: 기본기 — Claude Code와 대화하기

CLI 환경에서 파일을 다루고, 모드를 전환하고, 프로젝트 메모리를 설정하는 실전 기초.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 2.1 | [2.1-files-and-input.md](./2.1-files-and-input.md) | @파일 참조, 이미지 입력, 다중 출력 패턴 | J |
| 2.2 | [2.2-modes-and-depth.md](./2.2-modes-and-depth.md) | Edit/Auto-Accept/Plan 모드, think/ultrathink | J → P |
| 2.3 | [2.3-project-memory.md](./2.3-project-memory.md) | 메모리 계층 구조, PM 프로젝트용 CLAUDE.md 작성법 | P |
| 2.4 | [2.4-custom-subagents.md](./2.4-custom-subagents.md) | .claude/agents/ 파일 작성, 엔지니어/경영진/리서처 에이전트 | P → L |
| 2.5 | [2.5-agent-teams.md](./2.5-agent-teams.md) | 에이전트 팀: 멀티 에이전트 병렬 협업, Delegate 모드, 태스크 의존성 | P → L |
| 2.6 | [2.6-human-in-the-loop.md](./2.6-human-in-the-loop.md) | Human-in-the-Loop: AI 파트너 철학, 루프 깊이 프레임워크, 가드레일 설계 | 모든 레벨 |

---

### Part 3: 고급 설정 — 워크플로우 자동화 인프라

Claude Code의 자동화 인프라를 구축하고 고도화하는 심화 설정. MCP 연동, 프로젝트 메모리 심화, 슬래시 커맨드, 커스텀 스킬, 외부 자동화를 다룹니다.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 3.1 | [3.1-mcp-integration.md](./3.1-mcp-integration.md) | MCP 연동: Notion/Linear/Slack/GitHub를 하나의 터미널에서 연결 | P → L |
| 3.2 | [3.2-claude-md-deep-dive.md](./3.2-claude-md-deep-dive.md) | CLAUDE.md 심화: 폴더 구조, YAML front matter, AI Evals, 5축 프레임워크 | P → L |
| 3.3 | [3.3-slash-commands.md](./3.3-slash-commands.md) | 슬래시 커맨드: /today, /prd, /status 등 PM 반복 워크플로우 자동화 | P → L |
| 3.4 | [3.4-custom-skills.md](./3.4-custom-skills.md) | 커스텀 스킬: SKILL.md 기반 재사용 워크플로우 패키지 저장·관리·팀 공유 | P → L |
| 3.5 | [3.5-automation-n8n.md](./3.5-automation-n8n.md) | 외부 자동화: n8n으로 스케줄/이벤트 기반 워크플로우 구축 | P → L |

---

### Part 4: Discovery — 문제 발견

유저 리서치 데이터 분석과 경쟁사 분석을 Claude Code로 수행하는 실전 워크스루.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 4.1 | [4.1-discovery-user-research.md](./4.1-discovery-user-research.md) | CSV/설문 분석, 인터뷰 합성, PM 판단 포인트 | P |
| 4.2 | [4.2-discovery-competitive-analysis.md](./4.2-discovery-competitive-analysis.md) | 구조화된 분석, 멀티에이전트 병렬 분석, 감성 분석 | P → L |

---

### Part 5: Definition — 해결책 정의

PRD 작성과 전략 문서 작성을 Claude Code와의 대화를 통해 만들어가는 과정.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 5.1 | [5.1-definition-write-prd.md](./5.1-definition-write-prd.md) | 4단계 워크플로우, 반문 기반 대화, 멀티에이전트 리뷰 | P |
| 5.2 | [5.2-definition-product-strategy.md](./5.2-definition-product-strategy.md) | Diagnosis → Guiding Policy → Coherent Actions | P → L |

---

### Part 6: Delivery — 직접 만들고 보여주기

PM이 직접 프로토타입을 만들고, 비주얼 에셋을 생성하고, 배포까지 하는 실전 경험.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 6.1 | [6.1-delivery-vibe-coding.md](./6.1-delivery-vibe-coding.md) | 의도 기술 → Claude 구현 → PM 리뷰 루프 | J → P |
| 6.2 | [6.2-delivery-visual-assets.md](./6.2-delivery-visual-assets.md) | PM을 위한 5가지 비주얼 에셋 유형, Gemini API 연동 | P |
| 6.3 | [6.3-delivery-github-deploy.md](./6.3-delivery-github-deploy.md) | PM을 위한 Git 기초, Vercel 배포, 모니터링 | P |

---

### Part 7: Growth — 측정과 운영

실험 분석, KPI 대시보드, AI 옵저빌리티를 통해 데이터 드리븐 의사결정을 가속화하는 방법.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 7.1 | [7.1-growth-experiment-analysis.md](./7.1-growth-experiment-analysis.md) | A/B 테스트 분석, Impact 공식, ROI 시나리오 | P → L |
| 7.2 | [7.2-growth-kpi-dashboard.md](./7.2-growth-kpi-dashboard.md) | OMTM, KPI 정의 카드, 자동화 스크립트, 알림 체계 | L |
| 7.3 | [7.3-ai-observability.md](./7.3-ai-observability.md) | AI Observability: Helicone/LangSmith 기반 프로덕션 모니터링 | L |

---

### Part 8: 전략과 성장 경로

AI 제품 전략 프레임워크와 AI 네이티브 PM으로 성장하기 위한 로드맵.

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 8.1 | [8.1-ai-product-strategy.md](./8.1-ai-product-strategy.md) | AI 제품 전략: 4D 프레임워크 (Direction/Differentiation/Design/Deployment) | L |
| 8.2 | [8.2-growth-path.md](./8.2-growth-path.md) | J/P/L 로드맵, Before/After, 팀 도입 가이드 | 모든 레벨 |

---

### Appendix: 실전 연습

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| A.1 | [A.1-running-scenario.md](./A.1-running-scenario.md) | 하나의 제품으로 Discovery → Definition → Delivery → Growth 전체 흐름 체험 | P → L |
| A.2 | [A.2-level3-exercises.md](./A.2-level3-exercises.md) | 자동화/증강/직접판단 프레임워크 기반 실제 프로젝트 적용 | P → L |
| A.3 | [A.3-usecase-scenarios.md](./A.3-usecase-scenarios.md) | 마켓 사이징, 피드백 합성, M&A 실사 등 6가지 PM 실전 시나리오 | P → L |
| A.4 | [A.4-usecase-daily-briefing.md](./A.4-usecase-daily-briefing.md) | 크로스 툴 일일 브리핑 자동화 (Slack + Linear + Notion + GitHub) | J → P |
| A.5 | [A.5-usecase-status-report.md](./A.5-usecase-status-report.md) | 프로젝트 상태 보고서 자동 생성 및 이해관계자별 변형 | J → P |
| A.6 | [A.6-usecase-battle-cards.md](./A.6-usecase-battle-cards.md) | 경쟁사 배틀 카드 라이브러리 구축 및 월간 자동 업데이트 | P → L |
| A.7 | [A.7-usecase-customer-personas.md](./A.7-usecase-customer-personas.md) | 행동 데이터 클러스터링 기반 고객 페르소나 구축 | P → L |
| A.8 | [A.8-usecase-investment-memo.md](./A.8-usecase-investment-memo.md) | 비즈니스 케이스 / 투자 메모 작성 및 이사회 Q&A 시뮬레이션 | P → L |
| A.9 | [A.9-usecase-process-flowchart.md](./A.9-usecase-process-flowchart.md) | Mermaid 기반 제품 프로세스 플로우차트 문서화 | J → P |
| A.10 | [A.10-usecase-content-adaptation.md](./A.10-usecase-content-adaptation.md) | 릴리즈 콘텐츠의 6채널 동시 적응 및 발행 자동화 | J → P |

---

## 학습 원칙

1. **입력 → 응답 → 판단**: 모든 모듈은 실제 터미널 세션을 따라갑니다
2. **PM이 판단하는 지점**: Claude가 할 수 없는 것, PM만이 할 수 있는 것을 명확히 합니다
3. **Before/After**: 각 모듈에서 PM의 역할이 어떻게 변하는지를 보여줍니다
4. **점진적 난이도**: Part 1의 설치부터 Part 8의 전략까지 자연스럽게 상승합니다

---

## 빠른 시작

- **"Claude Code가 뭔지 모르겠어"** → [1.2-what-is-claude-code.md](./1.2-what-is-claude-code.md)
- **"일단 설치부터 하고 싶어"** → [1.3-install-and-first-run.md](./1.3-install-and-first-run.md)
- **"MCP로 도구를 연결하고 싶어"** → [3.1-mcp-integration.md](./3.1-mcp-integration.md)
- **"슬래시 커맨드로 업무를 자동화하고 싶어"** → [3.3-slash-commands.md](./3.3-slash-commands.md)
- **"자주 쓰는 워크플로우를 저장하고 싶어"** → [3.4-custom-skills.md](./3.4-custom-skills.md)
- **"PRD 작성에 바로 써보고 싶어"** → [5.1-definition-write-prd.md](./5.1-definition-write-prd.md)
- **"프로토타입을 직접 만들어보고 싶어"** → [6.1-delivery-vibe-coding.md](./6.1-delivery-vibe-coding.md)
- **"AI 제품 전략을 체계적으로 세우고 싶어"** → [8.1-ai-product-strategy.md](./8.1-ai-product-strategy.md)
- **"팀에 도입하는 방법이 궁금해"** → [8.2-growth-path.md](./8.2-growth-path.md)
- **"다양한 PM 실전 시나리오를 체험하고 싶어"** → [A.3-usecase-scenarios.md](./A.3-usecase-scenarios.md)
- **"전체 PM 워크플로우를 한 번에 보고 싶어"** → [A.1-running-scenario.md](./A.1-running-scenario.md)
- **"CLAUDE.md를 바로 세팅하고 싶어"** → [CLAUDE-md-starter.md](./templates/CLAUDE-md-starter.md) 복사 후 커스터마이징
- **"슬래시 커맨드를 바로 쓰고 싶어"** → [README.md](./templates/README.md) 에서 `/today`, `/prd`, `/status` 설치
- **"샘플 데이터로 실습하고 싶어"** → [README.md](./samples/README.md) 에서 CSV/JSON 데이터 활용

---

*이 가이드는 Claude Code의 실전 활용을 통해 PM의 일하는 방식을 재설계하기 위해 작성되었습니다.*


---

> **© 2026 김생근 (Sanguine Kim)** | AI Agent Lead & AI Tutor
> 본 자료는 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 라이선스를 따릅니다.
> 교육·학술 목적 자유 이용 가능 | 상업적 이용 시 별도 라이선스 필요
> 강의·기업 교육·상업적 활용 문의: kimsanguine@gmail.com
