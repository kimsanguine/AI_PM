---
title: "LangGraph vs RAG 실습 강의 — 채용 시장 리서치와 커리큘럼 결정"
type: research
claude_model: claude-opus-4-8
last_updated: 2026-10-19
status: draft
---

# LangGraph vs RAG 실습 강의 — 채용 시장 리서치와 커리큘럼 결정

> 질문: LangGraph 또는 RAG 실습 강의를 준비 중이다. 무엇을 가르쳐야 학생의 취업과 실력에 가장 도움이 되는가?
>
> 결론: "LangGraph냐 RAG냐"는 틀린 선택지다. RAG는 풀어야 할 문제이고 LangGraph는 도구다. 시장은 두 가지를 같이 요구한다. 취업에 직결되는 것은 "신뢰할 수 있는 에이전트 시스템을 끝까지 배포하고 측정해 본 증거"다. 리서치 결과는 이 방향을 지지했고, 동시에 처음 가설 두 개를 기각했으며, 신입 공고가 전체의 약 1할뿐이라는 사실을 새로 드러냈다.

---

## 1. 리서치 설계

### 1.1 처음 세운 가설

| # | 가설 | 출처 |
|---|---|---|
| H1 | 공고 키워드에서 RAG가 가장 빈번하고, LangChain/LangGraph가 그다음이다 | 경험 기반, 근거 없음 |
| H2 | 면접에서는 "왜 그 설계를 택했고 어떻게 품질을 측정했나"를 묻는다 | 경험 기반, 근거 없음 |
| H3 | 튜토리얼 복제 프로젝트는 걸러진다 | 경험 기반, 근거 없음 |
| H4 | 관리형 에이전트 플랫폼 확산으로 LangGraph 비중이 줄 수 있다 | 우려 |
| H5 | 긴 컨텍스트와 관리형 검색이 순진한 RAG를 대체한다 | 우려 |

### 1.2 방법

1. JobKorea 전문 검색으로 키워드별 공고 수를 수집했다 (2026-10-18 스냅샷).
2. 국내 공고 39건의 원문을 읽어 19개 기술 키워드의 등장 여부를 O/X로 코딩했다. 본문이 비어 있는 6건은 집계에서 제외해 33건을 분석했다.
3. 미국 데이터는 Lightcast가 Stanford AI Index 2026에 제공한 1차 자료를 사용했다.

### 1.3 한계

- 원티드, 사람인, 점핏 검색, 인디드는 접근이 차단되어 표본이 JobKorea 중심이다. 스타트업 비중이 과소 추정됐을 수 있다.
- 33건 중 약 22건이 2026년 공고이고 나머지는 2024~2025년이다. 목표였던 50건에는 못 미쳤다.
- 전문 검색 건수에는 노이즈가 섞여 있다 (예: 제약사 수시채용 공고가 모든 검색어에 등장). 자릿수 비교로만 사용한다.
- "LLM 평가" 검색 수는 검색어 특성상 신뢰할 수 없어 제외했다.

---

## 2. 결과

### 2.1 키워드별 공고 수 (JobKorea, 2026-10-18)

| 검색어 | 공고 수 |
|---|---|
| LLM | 1,280 |
| RAG + LLM | 478 |
| LLM agent | 430 |
| 파인튜닝 + LLM | 362 |
| LangChain | 177 |
| LangGraph | 149 |
| MCP + LLM | 134 |
| 벡터DB | 84 |
| LLM 신입 | 141 |

LangGraph가 LangChain의 84% 수준이다. 2년 전이라면 상상하기 어려운 비율이다. "LLM 신입"은 "LLM"의 11%다.

### 2.2 공고 원문 33건 키워드 코딩

| 키워드 | 건수 | 비율 |
|---|---|---|
| RAG | 26 | 79% |
| 에이전트 구축 (직무명 또는 주요업무) | 23 | 70% |
| LangChain | 17 | 52% |
| 벡터DB | 12 | 36% |
| LangGraph | 11 | 33% |
| Docker / K8s | 11 | 33% |
| FastAPI / REST API | 10 | 30% |
| 클라우드 (AWS, GCP, Azure) | 9 | 27% |
| LLMOps / MLOps | 8 | 24% |
| 평가 (지표, 파이프라인, 벤치마크) | 7 | 21% |
| 파인튜닝 (LoRA, RLHF 등) | 6 | 18% |
| RAG 심화 (GraphRAG, Hybrid Search, OCR, Document Parse) | 6 | 18% |
| 프롬프트 엔지니어링 | 5 | 15% |
| MCP | 4 | 12% |
| 관측 (LangSmith, Langfuse, tracing) | 4 | 12% |
| AI 코딩 도구 (Claude Code, Cursor) | 2 | 6% |

신입 지원 가능 공고는 33건 중 5건이다. 그중 2건은 석사를 요구하거나 우대한다.

### 2.3 미국 (Lightcast, Stanford AI Index 2026)

| 항목 | 수치 |
|---|---|
| AI 스킬 언급 공고 비율 | 2.5% (전년 대비 +55%) |
| Agentic AI 스킬 비율 | 2024년 0.06% → 2025년 0.23% (+280%, 약 90,000건) |
| Python 언급 공고 | 258,674건 (1위) |
| LangGraph | "enormous growth" (수치 미공개) |

RAG 2,885→12,609건, LangGraph 194→4,294건(2024→2025)이라는 수치는 2차 자료에만 있어 **확인 필요** 라벨을 단다.

---

## 3. 가설 검증

| 가설 | 결과 | 근거 |
|---|---|---|
| H1 RAG 최빈, LangChain/LangGraph 다음 | 확인 | 2.1, 2.2 |
| H2 평가 역량이 면접 변별 요건 | 부분 확인 | 평가는 21%지만 네이버(필수), SKT, 아이제라 등 상위 공고에 집중. 소규모 SI 공고는 태그만 나열 |
| H3 튜토리얼 복제는 걸러진다 | 검증 불가 | 공고 텍스트로는 알 수 없음. 근거 없음 |
| H4 관리형 플랫폼이 LangGraph를 대체 | 기각 | LangGraph 149건, Lightcast "enormous growth" |
| H5 긴 컨텍스트가 RAG를 대체 | 기각 | RAG 79%. 다만 요구 내용이 깊어짐 (3.1) |

### 3.1 예상하지 못한 발견

**신입 공고가 매우 적다.** LLM 공고의 약 11%만 신입 가능이고, 그중 상당수가 석사를 요구한다 (엔티엘헬스케어, LG에너지솔루션, NHN은 석사 또는 경력 2년, 제논은 석사 또는 학사+1년). 수강생은 "경력 2~3년처럼 보이는 증거"를 만들어야 한다.

**2026년 공고의 상당수가 SI·파견·프리랜서다.** 판교 상주, SK하이닉스 파견, 자동차 AI Agent 구축, 계약직 LangGraph 개발 등이다. 이 시장의 요구는 Python + LangGraph + RAG + FastAPI + Docker라는 매우 실무적인 묶음이다. 부트캠프 수료생의 현실적 진입 경로가 여기다.

**RAG의 요구 내용이 깊어졌다.** GraphRAG(3건), Hybrid Search, OpenSearch, Document Parse/OCR이 등장한다. 순진한 RAG로는 변별이 안 된다. 변별은 검색 품질에서 난다.

**AI 코딩 도구가 요건에 들어왔다.** 네이버는 "AI 코딩 도구 활용 경험"을 필수역량에, 블랙피그에이아이는 Claude Code와 Cursor를 스킬 태그에 적었다.

---

## 4. 커리큘럼 결정

### 4.1 처음 안에서 바뀐 것

| 항목 | 처음 안 | 수정 | 이유 |
|---|---|---|---|
| LangGraph | 오케스트레이션 층, 교체 가능 | 필수 | 33%, LangChain의 84% |
| RAG 깊이 | 청킹·하이브리드·리랭킹 | 문서 파싱(OCR) + 하이브리드 + GraphRAG 맛보기 | RAG 심화 18%, 변별 지점 |
| 배포 | 6단계에 포함 | 독립 모듈 (FastAPI + Docker + 클라우드 1종) | 각 30% 내외, SI 시장 요건 |
| 평가 | 핵심 변별 | 유지, "상위 회사 진입용"으로 위치 조정 | 21%, 상위 공고 집중 |
| 파인튜닝 | 없음 | 제외 확정 | 18%, 대부분 우대 또는 리서치 직군 |
| 프롬프트 엔지니어링 | 없음 | 단독 모듈 제외 | 15%, 단독 직무 공고 감소 |
| AI 코딩 도구 | 없음 | 작업 방식으로 전 주차 적용 | 네이버·블랙피그 요건 |

### 4.2 주차별 구성 (8주)

| 주차 | 주제 | 산출물 |
|---|---|---|
| 1 | 공고 50건 직접 집계 + 평가셋 30문항 작성 | 시장 리포트, 평가 데이터셋 |
| 2 | RAG 베이스라인 + PDF/OCR 문서 파싱 | 베이스라인 점수 |
| 3 | 하이브리드 검색(BM25 + 벡터), 리랭킹, 메타데이터 필터, 재측정 | 개선 전후 비교표 |
| 4 | LangGraph 상태 그래프, agentic RAG, 도구 호출, MCP 연동 | 그래프 설계 문서 |
| 5 | Human-in-the-loop, 체크포인트, 메모리, 멀티에이전트 1회 | 중단·재개 데모 |
| 6 | FastAPI + Docker + 클라우드 배포, Langfuse 관측 | 배포 URL, 트레이스 |
| 7 | 평가 파이프라인을 CI에 넣기, 비용·지연 측정 | 회귀 테스트 리포트 |
| 8 | 프레임워크 없이 재구현 + 실패 분석 글 | 포트폴리오 완성 |

8주차가 핵심이다. LangGraph는 2년 뒤 다른 것으로 바뀔 수 있다. 프레임워크가 숨기는 것이 무엇인지 아는 학생만 프레임워크가 바뀌어도 살아남는다.

### 4.3 신입 문제의 해법

공고가 요구하는 "경력 2년"을 포트폴리오로 대신 증명하는 것이 강의의 목표다. 네 가지가 한 묶음이어야 한다.

1. 동작하는 배포 URL
2. 개선 전후 점수가 있는 평가 리포트
3. 운영 트레이스 (Langfuse 등)
4. 실패 사례를 분석한 글 한 편

1주차 공고 집계 과제는 학생이 자기 목표 공고를 직접 고르게 만드는 장치이기도 하다.

### 4.4 경쟁 강의와의 차별 지점

| 경쟁군 | 가르치는 것 | 비어 있는 것 |
|---|---|---|
| 국내 부트캠프, 인프런, 패스트캠퍼스 | 프레임워크 사용법, 데모 챗봇 | 평가, 실패 분석, 운영 |
| LangChain Academy, DeepLearning.AI | 공식 사용법, 무료 | 자기 데이터 적용, 설계 판단 |
| Maven 계열 (예: AI Evals 강의) | 평가와 에러 분석 | 한국어, 국내 취업 맥락 |

프레임워크 사용법은 공식 문서와 무료 강의로 충분하다. 유료 강의의 차별 가치는 "판단"과 "실패 경험"이다.

---

## 5. 미확인 사항과 다음 행동

| 항목 | 상태 | 다음 행동 |
|---|---|---|
| 원티드·사람인 표본 | 미확보 | 강의 1주차 학생 과제로 보완 |
| 대기업 평가 요구의 일반화 | 네이버 1건 | 카카오·네이버·LG 공고 추가 수집 |
| 면접 질문 실태 (H2, H3) | 근거 없음 | 수료생·현직자 인터뷰 5명 |
| 미국 RAG/LangGraph 공고 수 | 2차 자료 | AI Index 원문 확인 |

---

## 부록 A. 공고별 코딩 결과 (33건)

| # | 회사 | 직무 | 경력 | 시기 | 주요 키워드 |
|---|---|---|---|---|---|
| 1 | 스카이월드와이드 | Knowledge Graph & Ontology Engineer | 6~9년 | 2026-02 마감 | RAG/GraphRAG, LangChain·LangGraph(우대), Neo4j, MLOps |
| 2 | 바이스벌사 | 생성형 AI/LLM 엔지니어 | 3~5년 | 2025-05 마감 | RAG, LangChain·LangGraph(필수), MCP, AWS/GCP, 프롬프트, 멀티모달 |
| 3 | 유니드컴즈 | AI 엔지니어 | 3~10년 | 2025-03 마감 | LangChain·LlamaIndex, RAG, 자율 에이전트, Gradio/HF, 포트폴리오 필수 |
| 4 | 엔닷라이트 | LLM RAG 개발자 | 2~10년 | 2025-06 마감 | RAG, Agent, 파인튜닝, 프롬프트/체인 |
| 5 | 다이얼로그디자인에이전시 | AI/NLP R&D Engineer | 3~5년 | 2024-04 마감 | RAG, 파인튜닝, LangChain·LlamaIndex, 평가 지표 설계 |
| 6 | 아이제라 | AI 에이전트 엔지니어 | 5년+ | 2025-11 마감 | RAG, FAISS/Pinecone, LangChain·LlamaIndex·AutoGen, MCP, 도구호출, 평가·가드레일, 비용/지연, FastAPI, Docker/K8s, A/B |
| 7 | 네이션에이 | 서비스 프롬프트 엔지니어 | 신입 | 2025-10 마감 | LangSmith·Langfuse(필수), Dify/Langflow, 프롬프트, RAG(우대), 평가 시스템(우대) |
| 8 | 피피에스 | LLM/RAG AI 개발 | 5년+ | 2026-01 마감 | LLM, RAG, Agent, VectorDB (태그) |
| 9 | 바이트사이즈 | LLM RAG 및 AI Agent 개발 | 신입 | 2026-02 접수 | Python, RAG, OpenAI/LangChain/LlamaIndex, Qdrant/FAISS |
| 10 | 싸이버로지텍 | AI 에이전트 핵심 개발자 | 경력 | 2026-05 마감 | RAG, FastAPI, LangChain·LangGraph·LangSmith, 멀티에이전트, Modular RAG, 벡터검색·LLMOps·파인튜닝(우대) |
| 11 | NHN LLM서비스개발팀 | LLM 기술 개발 (LLM/Agent) | 2년+ 또는 석사 | 2026-11 마감 | RAG 파이프라인(청킹/임베딩/검색 품질 튜닝), Agent orchestration, LoRA(우대) |
| 12 | 카카오 | AI Research Engineer (Agentic Search LLM) | 신입·경력 | 상시 | RL(PPO/GRPO), 실험 분석. 프레임워크보다 ML 원리 |
| 13 | 제논 | AI Engineer (생성형 AI Agent) | 석사 또는 학사+1년 | 확인 필요 | LangChain·LangGraph 기반 RAG, 에이전트 |
| 14 | 인포그랩 | AI 워크플로 자동화 엔지니어 | 확인 필요 | 확인 필요 | n8n, LangChain·LangGraph, Pinecone/Weaviate/Qdrant/pgvector, K8s, CI/CD |
| 15 | 네이버 | AI 에이전트 엔지니어 | 경력 | 2026-10-12 마감 | RAG, 벡터DB, LangChain/LangGraph/AutoGen 1종 필수, tool-calling, 평가 파이프라인(필수), 벤치마크, 비용/지연, LangSmith·Langfuse·멀티에이전트·안전성·RLHF/GRPO·K8s(우대), AI 코딩 도구 |
| 16 | SK바이오팜 | AI Engineer (AX팀) | 5~15년 | 2026-08 마감 | RAG, 멀티에이전트, 프롬프트, 관측성(logging/metrics/tracing), AWS/Azure, Docker, K8s(우대) |
| 17 | SK텔레콤 | AI Agent 플랫폼 엔지니어 | 2년+ 계약직 | 2026-06 마감 | 평가 데이터셋/파이프라인, Python 백엔드/REST, Docker, 인증/민감정보 |
| 18 | 블랙피그에이아이 | AI/ML 엔지니어 (LLM·에이전트) | 3~5년 | 2026 | Python, LLM, Claude Code, Cursor, OCR, RAG, Hybrid Search, LangGraph |
| 19 | 콘센트릭스서비스코리아 | LLM/Agent Engineer | 5년+ | 2026-11 마감 | Python, FastAPI, LangChain, LangGraph |
| 20 | DXT | AI Agent/LLM Engineer | 5년+ | 2026-10 마감 | RAG, LLMOps, LangChain, VectorDB |
| 21 | 페보 | Senior AI Agent/LLM 엔지니어 | 5년+ | 2026-10 마감 | AWS, RAG, AI Agent |
| 22 | 퀀텀씨엔에스 | Agent AI 개발자 | 경력 | 상시 | K8s, FastAPI, RAG, LLMOps, MCP, OpenSearch, LangChain, LangGraph, VectorDB |
| 23 | 디딤 | AI Agent/LLM 기반 개발자 | 3년+ | 2026-11 마감 | Java/Spring/React, FastAPI (LLM 세부 요건 없음) |
| 24 | 서치독 | AI 개발자 (LLM·Agent·AWS Bedrock) | 3년+ 계약직 | 2026-11 마감 | AWS Bedrock, RAG, MLOps, NLP |
| 25 | 더씨에스알 | AI 엔지니어 (LLM·RAG) | 1년+ | 2026-11 마감 | RAG(직무명), 스킬 태그 불일치 |
| 26 | 에이아이스타 | LLM·RAG 엔지니어 | 3년+ | 2026-12 마감 | RAG, Vector DB, Python, NLP, API |
| 27 | 엔티엘헬스케어 | LLM/RAG 개발자 | 신입·3년+, 석사 | 2026-10 마감 | FastAPI, RAG, CI/CD, LLM 서빙, GPU 운영 |
| 28 | 메타펫 | AI 엔지니어 (LLM·RAG·GraphRAG) | 신입·경력 | 2026-11 마감 | AWS, Docker, Java, PostgreSQL, RAG, LLMOps, GraphRAG |
| 29 | 넥스인테크놀로지 | AI Core Engineer (RAG & LLM) | 신입·3년+ | 2026-11 마감 | RAG, LLMOps, LangChain, vLLM |
| 30 | 아크론 | AI 에이전트 개발 (판교 상주 프리랜서) | 4년+ | 2026-11 마감 | OCR, RAG, Document Parse, MCP, LangChain, LangGraph |
| 31 | 컴스페이스컨설팅 | AI Agent 개발 (계약직) | 5년+ | 2026-11 마감 | LangGraph, LangChain, Docker, K8s |
| 32 | 띵스파이어 | SK하이닉스 파견 AI Agent 개발자 | 3년+ | 상시 | AWS, Docker, K8s, REST API, MLOps, NLP |
| 33 | 사이버테크프랜드 | RAG/LLM/AI 챗봇 개발 | 3년+ | 2026-10 마감 | Docker, RAG, REST API, LangChain, LlamaIndex, Vector DB, Embedding |

본문이 비어 있어 집계에서 제외한 공고: NHN(JobKorea 페이지), SK AX, LG에너지솔루션, 에프앤가이드(신입 인턴), 메가존클라우드, 블랙피그에이아이(JobKorea 페이지).

---

## 부록 B. 출처

- [잡코리아 'LLM agent' 검색](https://www.jobkorea.co.kr/Search?stext=LLM+agent&tabType=recruit&Page_No=0)
- [잡코리아 'llm' 검색](https://www.jobkorea.co.kr/Search/?stext=llm)
- [잡코리아 'RAG LLM' 검색](https://www.jobkorea.co.kr/Search?stext=RAG+LLM&tabType=recruit&Page_No=0)
- [잡코리아 'LangGraph' 검색](https://www.jobkorea.co.kr/Search?stext=LangGraph&tabType=recruit&Page_No=0)
- [네이버 AI 에이전트 엔지니어 공고](https://zighang.com/recruitment/0451a237-7301-445f-adc6-6032b301b3e9)
- [SK바이오팜 AI Engineer 공고](https://www.skcareers.com/Recruit/Detail/R261663)
- [SK텔레콤 AI Agent 플랫폼 엔지니어 공고](https://linkareer.com/activity/326451)
- [아이제라 AI 에이전트 엔지니어 공고](https://jumpit.saramin.co.kr/position/52131589)
- [네이션에이 서비스 프롬프트 엔지니어 공고](https://jumpit.saramin.co.kr/position/51792610)
- [바이스벌사 생성형 AI/LLM 엔지니어 공고](https://jumpit.saramin.co.kr/position/50533504)
- [스카이월드와이드 Knowledge Graph & Ontology Engineer 공고](https://jumpit.saramin.co.kr/position/52967506)
- [싸이버로지텍 AI 에이전트 개발자 공고](https://www.jobplanet.co.kr/job/search?posting_ids%5B%5D=1303537)
- [바이트사이즈 신입 공고](https://linkareer.com/activity/300738)
- [groupby AI 채용 목록 (블랙피그에이아이 등)](https://groupby.kr/jobs/ai)
- [카카오 AI Research Engineer 공고](https://careers.kakao.com/jobs/P-14519?part=TECHNOLOGY&company=KAKAO&page=1)
- [제논 AI Engineer 공고](https://www.wanted.co.kr/wd/215978)
- [Lightcast, The Stanford AI Index Report 2026](https://lightcast.io/resources/research/stanford-ai-index-2026)
- [Lightcast, Four Takeaways from the 2026 Stanford AI Index](https://lightcast.io/resources/blog/stanford-ai-2026)
- [AI Engineering Jobs 2026 (2차 자료, 확인 필요)](https://productleadersdayindia.org/blogs/ai-engineering-jobs-skills/ai-engineering-jobs-skills-hiring-wave.html)
