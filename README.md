# 🚀 AI 네이티브 PM을 위한 Claude Code 실전 가이드

> **"도구를 배우는 것이 아니라, PM의 일하는 방식을 재설계한다."**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 이 가이드는 무엇인가요?

Claude Code(CLI 기반 AI 에이전트)를 활용하여 PM이 **Discovery → Definition → Delivery → Growth** 전체 제품 개발 사이클에서 일하는 방식을 어떻게 변화시킬 수 있는지를 다루는 실전 가이드입니다.

단순한 도구 사용법이 아닌, **실제 터미널 입력 → Claude 응답 → PM 판단**의 워크스루를 통해 학습합니다.

```
기존 PM 워크플로우:          AI 네이티브 PM 워크플로우:
━━━━━━━━━━━━━━━━━━          ━━━━━━━━━━━━━━━━━━━━━━━━━
문서 작성      40%           문제 정의 & 검증 설계  50%
회의 & 조율    30%    →      전략적 의사결정        25%
데이터 취합    20%           실행 오케스트레이션    20%
전략 사고      10%           AI 워크플로우 관리      5%
```

---

## 누구를 위한 가이드인가요?

| 레벨 | 설명 | 권장 학습 경로 |
| --- | --- | --- |
| **J (Junior)** | PM 경력 0~2년, AI 도구 경험 적음 | Part 1 → 2 → 4 순서대로 |
| **P (Practitioner)** | PM 경력 3~7년, AI 도구 일부 사용 중 | Part 1 훑고 → Part 3~6 집중 |
| **L (Lead)** | PM 경력 7년+, 팀/조직 리딩 | Part 1 훑고 → Part 5~8 집중 |

---

## 목차

### Part 1: 시작하기 — 왜 지금, AI 네이티브 PM인가

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 1.1 | [왜 지금인가](./1.1-why-now.md) | PM 역할 변화, 자동화/증강/직접판단 프레임워크 | 모든 레벨 |
| 1.2 | [Claude Code란 무엇인가](./1.2-what-is-claude-code.md) | ChatGPT/Copilot과의 차이, CLI의 4가지 장점 | 모든 레벨 |
| 1.3 | [설치와 첫 실행](./1.3-install-and-first-run.md) | 설치 가이드, 첫 대화 예시, 트러블슈팅 | J |

### Part 2: 기본기 — Claude Code와 대화하기

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 2.1 | [파일과 입력](./2.1-files-and-input.md) | @파일 참조, 이미지 입력, 다중 출력 패턴 | J |
| 2.2 | [모드와 깊이](./2.2-modes-and-depth.md) | Edit/Auto-Accept/Plan 모드, think/ultrathink | J → P |
| 2.3 | [프로젝트 메모리](./2.3-project-memory.md) | 메모리 계층 구조, CLAUDE.md 작성법 | P |
| 2.4 | [커스텀 서브에이전트](./2.4-custom-subagents.md) | 엔지니어/경영진/리서처 에이전트 구성 | P → L |
| 2.5 | [에이전트 팀](./2.5-agent-teams.md) | 멀티 에이전트 병렬 협업, Delegate 모드 | P → L |
| 2.6 | [Human-in-the-Loop](./2.6-human-in-the-loop.md) | AI 파트너 철학, 루프 깊이 프레임워크, 가드레일 설계 | 모든 레벨 |

### Part 3: 고급 설정 — 워크플로우 자동화 인프라

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 3.1 | [MCP 연동](./3.1-mcp-integration.md) | Notion/Linear/Slack/GitHub를 하나의 터미널에서 연결 | P → L |
| 3.2 | [CLAUDE.md 심화](./3.2-claude-md-deep-dive.md) | 폴더 구조, YAML front matter, 5축 프레임워크 | P → L |
| 3.3 | [슬래시 커맨드](./3.3-slash-commands.md) | /today, /prd, /status 등 반복 워크플로우 자동화 | P → L |
| 3.4 | [커스텀 스킬](./3.4-custom-skills.md) | SKILL.md 기반 재사용 워크플로우 패키지 | P → L |
| 3.5 | [외부 자동화 (n8n)](./3.5-automation-n8n.md) | 스케줄/이벤트 기반 워크플로우 구축 | P → L |

### Part 4: Discovery — 문제 발견

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 4.1 | [유저 리서치](./4.1-discovery-user-research.md) | CSV/설문 분석, 인터뷰 합성, PM 판단 포인트 | P |
| 4.2 | [경쟁사 분석](./4.2-discovery-competitive-analysis.md) | 구조화된 분석, 멀티에이전트 병렬 분석, 감성 분석 | P → L |

### Part 5: Definition — 해결책 정의

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 5.1 | [PRD 작성 (소크라틱 방법론)](./5.1-definition-write-prd.md) | 소크라틱 질문법, 반문 기반 대화, 멀티에이전트 리뷰 | P |
| 5.2 | [제품 전략 (Rumelt 전략 커널)](./5.2-definition-product-strategy.md) | Diagnosis → Guiding Policy → Coherent Actions | P → L |

### Part 6: Delivery — 직접 만들고 보여주기

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 6.1 | [바이브 코딩 + Pencil 연동](./6.1-delivery-vibe-coding.md) | 의도 기술 → Claude 구현 → PM 리뷰 루프 | J → P |
| 6.2 | [비주얼 에셋](./6.2-delivery-visual-assets.md) | 5가지 비주얼 에셋 유형, Gemini API 연동 | P |
| 6.3 | [GitHub 배포](./6.3-delivery-github-deploy.md) | Git 기초, Vercel 배포, 모니터링 | P |

### Part 7: Growth — 측정과 운영

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 7.1 | [실험 분석](./7.1-growth-experiment-analysis.md) | A/B 테스트 분석, Impact 공식, ROI 시나리오 | P → L |
| 7.2 | [KPI 대시보드](./7.2-growth-kpi-dashboard.md) | OMTM, KPI 정의 카드, 자동화 스크립트, 알림 체계 | L |
| 7.3 | [AI 옵저빌리티](./7.3-ai-observability.md) | Helicone/LangSmith 기반 프로덕션 모니터링 | L |

### Part 8: 전략과 성장 경로

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| 8.1 | [AI 제품 전략](./8.1-ai-product-strategy.md) | 4D 프레임워크 (Direction/Differentiation/Design/Deployment) | L |
| 8.2 | [성장 경로](./8.2-growth-path.md) | J/P/L 로드맵, Before/After, 팀 도입 가이드 | 모든 레벨 |

### Appendix: 실전 연습 & 유즈케이스

| # | 제목 | 핵심 내용 | 난이도 |
| --- | --- | --- | --- |
| A.1 | [러닝 시나리오](./A.1-running-scenario.md) | Discovery → Delivery → Growth 전체 흐름 체험 | P → L |
| A.2 | [Level 3 실습](./A.2-level3-exercises.md) | 자동화/증강/직접판단 프레임워크 기반 프로젝트 적용 | P → L |
| A.3 | [PM 실전 시나리오](./A.3-usecase-scenarios.md) | 마켓 사이징, 피드백 합성, M&A 실사 등 6가지 | P → L |
| A.4 | [일일 브리핑 자동화](./A.4-usecase-daily-briefing.md) | Slack + Linear + Notion + GitHub 크로스 툴 브리핑 | J → P |
| A.5 | [상태 보고서 자동화](./A.5-usecase-status-report.md) | 프로젝트 상태 보고서 자동 생성 및 이해관계자별 변형 | J → P |
| A.6 | [배틀 카드](./A.6-usecase-battle-cards.md) | 경쟁사 배틀 카드 라이브러리 구축 | P → L |
| A.7 | [고객 페르소나](./A.7-usecase-customer-personas.md) | 행동 데이터 클러스터링 기반 페르소나 구축 | P → L |
| A.8 | [투자 메모](./A.8-usecase-investment-memo.md) | 비즈니스 케이스 작성 및 이사회 Q&A 시뮬레이션 | P → L |
| A.9 | [프로세스 플로우차트](./A.9-usecase-process-flowchart.md) | Mermaid 기반 프로세스 문서화 | J → P |
| A.10 | [콘텐츠 적응](./A.10-usecase-content-adaptation.md) | 릴리즈 콘텐츠 6채널 동시 적응 및 발행 자동화 | J → P |

---

## 빠른 시작

```
"Claude Code가 뭔지 모르겠어"        → 1.2-what-is-claude-code.md
"일단 설치부터 하고 싶어"             → 1.3-install-and-first-run.md
"PRD 작성에 바로 써보고 싶어"         → 5.1-definition-write-prd.md
"프로토타입을 직접 만들어보고 싶어"     → 6.1-delivery-vibe-coding.md
"CLAUDE.md를 바로 세팅하고 싶어"      → templates/CLAUDE-md-starter.md
"샘플 데이터로 실습하고 싶어"          → samples/README.md
"전체 PM 워크플로우를 한 번에 보고 싶어" → A.1-running-scenario.md
```

---

## 프로젝트 구조

```
AI_PM/
├── 00-index.md                    # 전체 목차 및 학습 가이드
├── 1.1 ~ 1.3                      # Part 1: 시작하기
├── 2.1 ~ 2.6                      # Part 2: 기본기
├── 3.1 ~ 3.5                      # Part 3: 고급 설정
├── 4.1 ~ 4.2                      # Part 4: Discovery
├── 5.1 ~ 5.2                      # Part 5: Definition
├── 6.1 ~ 6.3                      # Part 6: Delivery
├── 7.1 ~ 7.3                      # Part 7: Growth
├── 8.1 ~ 8.2                      # Part 8: 전략과 성장
├── A.1 ~ A.10                     # Appendix: 실전 유즈케이스
├── samples/                       # 실습용 데이터
│   ├── ab-test-results.csv        # A/B 테스트 결과 샘플
│   ├── competitor-data.json       # 경쟁사 데이터 샘플
│   └── user-survey-results.csv    # 유저 서베이 결과 샘플
└── templates/                     # 바로 쓸 수 있는 템플릿
    ├── CLAUDE-md-starter.md       # CLAUDE.md 스타터 템플릿
    └── commands/                  # 슬래시 커맨드 템플릿
        ├── today.md               # /today — 일일 브리핑
        ├── prd.md                 # /prd — PRD 생성
        └── status.md              # /status — 상태 보고서
```

---

## 학습 원칙

1. **입력 → 응답 → 판단** — 모든 모듈은 실제 터미널 세션을 따라갑니다
2. **PM이 판단하는 지점** — Claude가 할 수 없는 것, PM만이 할 수 있는 것을 명확히 합니다
3. **Before/After** — 각 모듈에서 PM의 역할이 어떻게 변하는지를 보여줍니다
4. **점진적 난이도** — Part 1의 설치부터 Part 8의 전략까지 자연스럽게 상승합니다

---

## 주요 이론 프레임워크

이 가이드에서 다루는 핵심 이론과 방법론입니다.

| 프레임워크 | 출처 | 적용 챕터 |
| --- | --- | --- |
| 소크라틱 질문법 (Richard Paul & Linda Elder) | 비판적 사고 교육 | 5.1 PRD 작성 |
| Rumelt 전략 커널 (Good Strategy Bad Strategy) | Richard Rumelt, 2011 | 5.2 제품 전략 |
| Human-in-the-Loop (HITL/HOTL/HOOTL) | AI 협업 모델 | 2.6 HITL |
| 자동화/증강/직접판단 프레임워크 | 본 가이드 제안 | 1.1, A.2 |
| 4D AI 제품 전략 | 본 가이드 제안 | 8.1 AI 전략 |

---

## Contributing

이 가이드에 대한 피드백, 오류 수정, 추가 유즈케이스 제안을 환영합니다.

- **Issues**: 오류나 개선 제안은 [Issues](https://github.com/kimsanguine/AI_PM/issues)에 등록해 주세요
- **Pull Requests**: 직접 수정 후 PR을 보내주셔도 좋습니다

---

## License

이 프로젝트는 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 라이선스를 따릅니다.

- 교육·학술 목적 자유 이용 가능
- 상업적 이용 시 별도 라이선스 필요
- 강의·기업 교육·상업적 활용 문의: kimsanguine@gmail.com

---

**© 2026 김생근 (Sanguine Kim)** | AI Agent Lead & AI Tutor
