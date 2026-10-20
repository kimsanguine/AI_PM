---
title: "해커톤 O1 계획안 + O2·O3 실현 가능성 조사"
type: research
claude_model: claude-opus-4-8
last_updated: 2026-10-20
status: draft
related: 2026-10-llm-job-market-langgraph-rag.md
---

# 해커톤 O1 계획안 + O2·O3 실현 가능성 조사

> 전제: `2026-10-llm-job-market-langgraph-rag.md`의 채용 리서치에서 OCR·Document Parse, RAG 심화, 평가, 배포가 공고 요건으로 확인됐다. 이 문서는 그 요건에 맞는 OCR 파싱 해커톤 주제 3개 중 O1의 실행 계획과 O2·O3의 데이터 접근 가능성을 다룬다.
>
> 결론: O1은 바로 실행 가능하다. PDF 원문, XBRL 정답, 호출 한도 모두 확인됐다. O2는 실현 가능하지만 "표·레이아웃 정답"은 행정문서 OCR 데이터에 없으므로 다른 AI Hub 데이터와 짝지어야 한다. O3는 PDF 확보는 쉽지만 정답 라벨이 없어 평가 설계를 바꿔야 한다.

---

## Part A. O1 계획안 — 사업보고서 PDF 재무제표 표 추출, XBRL 정답 대조

### A.1 한 줄 정의

코스피 상장사 사업보고서 PDF에서 재무상태표·손익계산서·현금흐름표를 추출하고, 같은 보고서의 XBRL 재무제표를 정답으로 삼아 파서별 정확도를 측정한다.

### A.2 왜 이 주제인가

| 근거 | 내용 |
|---|---|
| 정답 라벨 비용 0 | 같은 보고서가 PDF와 XBRL 두 형태로 공시된다. 사람 라벨링 없이 셀 단위 정답을 만든다 |
| 채용 연결 | 에프앤가이드 금융 AI Agent, SK하이닉스 Market Intelligence, 금융 RAG 공고 전반 |
| 시장 공백 | PulseBench-Tab에서 한국어 표 추출은 제공자 간 편차 75%p 이상. 한국어 표 벤치마크가 없다 |
| 실무 재현 | 금융사가 실제로 하는 일(공시 PDF를 구조화해 DB에 넣기)과 같다 |

### A.3 검증된 데이터 경로

| 단계 | 엔드포인트 | 확인 결과 |
|---|---|---|
| 1. 회사 코드 | `opendart.fss.or.kr/api/corpCode.xml` | zip 안 XML, corp_code 8자리 |
| 2. 공시 목록 | `opendart.fss.or.kr/api/list.json` | rcept_no, 접수일자(rcept_dt) 확보 |
| 3. PDF 원문 | `dart.fss.or.kr/pdf/download/pdf.do?rcp_no=&dcm_no=` | **직접 확인**: `application/pdf`, 922KB 반환. 비공식 웹 경로 |
| 4. 정답(계정) | `opendart.fss.or.kr/api/fnlttSinglAcntAll.json` | XBRL 표준계정ID, 당기·전기·전전기 금액, BS/IS/CIS/CF/SCE 구분. 2015년 이후 |
| 5. 정답(원본) | `opendart.fss.or.kr/api/fnlttXbrl.xml` | XBRL 원본 zip. reprt_code 11011이 사업보고서 |
| 6. 보조 원문 | `opendart.fss.or.kr/api/document.xml` | 공시 원문 zip(XML/HTML). 표 HTML을 구조 정답(TEDS)으로 쓸 수 있다 |

호출 한도는 일 20,000건(응답코드 020)이고, 한 요청의 회사 수는 100건 이하(021)다. 인증키는 이메일 인증 후 발급된다. PDF 경로는 공식 API가 아니라 DART 웹의 다운로드 기능이므로 변경될 수 있고, 문서번호(dcm_no)는 뷰어 페이지(`dsaf001/main.do?rcpNo=`)에서 추출해야 한다.

### A.4 범위

| 항목 | 설정 | 이유 |
|---|---|---|
| 회사 | 코스피 시가총액 상위 50사 | 연결재무제표가 있어 CFS/OFS 구분 과제가 생긴다 |
| 보고서 | 최근 2개 사업연도 사업보고서 | 100 PDF. 해커톤 2일에 처리 가능한 규모 |
| 표 | 재무상태표, 손익계산서, 현금흐름표 | 표준계정ID 매칭률이 높다. 자본변동표는 셀 병합이 많아 제외 |
| 난이도 층 | 디지털 PDF / PDF를 300dpi 이미지로 변환한 뒤 OCR / 감사보고서 첨부 스캔본 | 같은 정답으로 세 난이도를 측정한다 |

### A.5 평가 설계

| 지표 | 정의 | 정답 출처 |
|---|---|---|
| 셀 정확도 | 계정명·기간이 일치하는 셀의 금액 일치율 | fnlttSinglAcntAll |
| 계정 recall | XBRL 표준계정 중 파서가 찾은 비율 | fnlttSinglAcntAll |
| 구조 유사도 | TEDS (Tree Edit Distance Similarity) | document.xml의 표 HTML |
| 숫자 환각률 | 정답에 없는 금액을 만들어낸 비율 | fnlttSinglAcntAll |
| 자기검증 통과율 | 자산 = 부채 + 자본 등 회계 항등식 통과율 | 파서 출력만으로 계산 |
| 비용·지연 | 페이지당 원화 비용, 초 | 로그 |

정규화 규칙을 먼저 정해야 한다. 단위(원, 천원, 백만원), 음수 표기(괄호, 마이너스), 계정명 동의어(매출액/수익), 전기 재작성 표시가 주요 함정이다. 이 규칙 자체가 팀의 산출물이다.

### A.6 파서 후보

| 구분 | 후보 | 비고 |
|---|---|---|
| 규칙 기반 | pdfplumber, camelot | 디지털 PDF 베이스라인 |
| 오픈소스 파서 | Docling, Marker, MinerU | 레이아웃 모델 포함 |
| 상용 API | Upstage Document Parse, Mistral OCR | 비용 측정 대상. Upstage는 한국어 문서에 강점이 있다는 논문 언급이 있으나 표 점수는 미공개 |
| VLM 직접 | 이미지를 LLM에 넣어 JSON 추출 | 환각률 측정의 핵심 비교군 |

### A.7 일정

| 단계 | 기간 | 할 일 |
|---|---|---|
| 사전 준비 | 본선 2주 전 | 주최 측: 50사 목록, rcept_no·dcm_no 매핑표, 정규화 규칙 초안, 평가 스크립트 공개. 참가자: OpenDART 키 발급 |
| 본선 1일차 | 오전 | PDF 수집, 베이스라인(pdfplumber) 점수 측정 |
| 본선 1일차 | 오후 | 파서 2종 이상 비교, 실패 사례 수집 |
| 본선 2일차 | 오전 | 선택한 파서 고도화(후처리, 표 재구성, 항등식 검증) |
| 본선 2일차 | 오후 | 리더보드 제출, 실패 분석 글 |
| 사후 | 1주 | 상위 팀 결과를 한국어 표 벤치마크 초안으로 정리 |

주최 측이 rcept_no·dcm_no 매핑표와 평가 스크립트를 미리 주지 않으면 참가자가 첫날 반나절을 스크래핑에 쓴다. 이 둘이 해커톤 품질을 가른다.

### A.8 산출물과 심사

| 산출물 | 심사 비중 |
|---|---|
| 리더보드 점수 (셀 정확도, recall, TEDS) | 40% |
| 실패 분석 글 (틀린 사례 분류, 원인, 대응) | 25% |
| 비용·지연 대비 정확도 표 | 15% |
| 재현 가능한 코드와 README | 10% |
| 배포된 데모 (PDF 업로드 → JSON) | 10% |

### A.9 리스크

| 리스크 | 대응 |
|---|---|
| PDF 다운로드 경로가 비공식 | 사전 준비 단계에서 100개 PDF를 주최 측이 미리 받아 둔다. 재배포는 공시 자료라 문제없으나 출처를 표기한다 |
| 연결(CFS)과 별도(OFS) 혼동 | 정답 조회 시 fs_div를 명시하고, PDF에서 어느 표를 읽었는지 팀이 표시하게 한다 |
| 분·반기 금액 혼동 | 사업보고서(11011)만 쓴다 |
| 접수일자 이전 데이터 사용 | rcept_dt 이후 데이터만 쓰는 규칙을 평가 스크립트에 넣는다 |
| 상용 API 비용 | 팀당 예산 상한을 정하고 비용을 점수에 반영한다 |

### A.10 참가자 사전 체크리스트

1. OpenDART 회원가입, 이메일 인증, 인증키 발급
2. corpCode.xml 받아 corp_code 추출 테스트
3. fnlttSinglAcntAll.json 1회 호출해 응답 구조 확인
4. 주최 측 제공 PDF 100개와 매핑표 다운로드
5. 평가 스크립트로 빈 제출물 채점해 파이프라인 확인

---

## Part B. O2 조사 — 저품질 스캔 행정문서 구조화

### B.1 판정

실현 가능하다. 다만 공공행정문서 OCR 데이터에는 표·레이아웃·키-값 라벨이 없다. "구조화" 정답은 다른 AI Hub 데이터에서 가져와야 한다.

### B.2 후보 데이터

| 데이터 | dataSetSn | 구축 | 규모 | 라벨 | 적합 용도 |
|---|---|---|---|---|---|
| 공공행정문서 OCR | 88 | 2020 | 90만 장, 2,500만 단어 | bbox + 텍스트. 인허가·주민자치·도시개발 등 13분야. 저품질 스캔, 수기·타자체 혼합 | 저품질 OCR 본 과제 |
| OCR 데이터(공공) | 71299 | 2022 | 61.5만 면 | bbox + 텍스트 + 서체 유형. 창원시·김해시·외교사료관 | 88의 대안. 더 최신 |
| 오피스 문서 생성 데이터 | 71811 | 2024 | PDF 10,261, JPG 47,072, JSON 30만 | **레이아웃 bbox(제목·본문·목록·표·차트·다이어그램) + plain_text**. 행정문서(결재형·계약형) 포함 | 레이아웃·표 영역 정답 |
| 표 이미지-텍스트 쌍 | 71709 | 2023 | 40.4만 표 | **표 HTML 원천** + 설명문·요약문. 공공누리 출처, 병합표 포함 | 표 구조(TEDS) 정답 |
| OCR 데이터(금융 및 물류) | 71301 | 2022 | 금융 5만 + 물류 10.8만 장 | 어절 폴리곤 + 텍스트. 신고서·청구서·위임장·송장·선하증권 | 서식 문서 변형 과제 |
| 금융업 특화 문서 OCR | 632 | 2021 | 5만 장 | 폴리곤 + bbox. 인쇄·손글씨 혼합 | 손글씨 변형 과제 |

### B.3 이용 조건 (AI Hub 공통)

| 항목 | 내용 |
|---|---|
| 신청 자격 | 내국인만. 국외 법인·개인은 별도 합의 필요 |
| 승인 | 일반 개방 데이터는 휴대폰 인증 후 자동 승인. 데이터셋별로 다를 수 있음 |
| 이용 범위 | 일반 개방 데이터는 영리·비영리 연구개발 허용. 일부 데이터는 비상업 한정, 공공데이터포털에는 "상업적 이용금지" 표기 사례도 있음. **데이터셋별 확인 필수** |
| 재배포 | 승인받지 않은 제3자에게 열람·제공·양도·판매 금지 |
| 출처 표시 | 한국지능정보사회진흥원 사업 결과임을 명시. 2차 저작물도 동일 |
| 다운로드 | API 다운로드, 분할 압축을 Linux 명령으로 병합. Windows는 WSL 필요 |
| 용량 | 모든 후보 페이지에 용량 미표기. 90만 장이면 수백 GB 가능성 |

### B.4 해커톤 설계 제안

| 항목 | 제안 |
|---|---|
| 과제 정의 | 저품질 스캔 행정문서에서 "문서 유형 분류 + 필드 추출(문서번호, 날짜, 발신기관, 제목, 표 영역)" |
| 정답 | 텍스트는 88/71299 라벨. 레이아웃·표 영역은 71811 라벨. 표 구조는 71709 HTML. 키-값 필드는 라벨이 없으므로 주최 측이 200장 샘플에 LLM 초안 + 사람 검수로 제작 |
| 배포 방식 | 재배포 금지이므로 각 팀이 직접 신청·다운로드. 주최 측은 "경량 샘플" 사용을 권장하고 전체 다운로드는 선택 |
| 시간 리스크 | 전체 데이터 다운로드가 하루 이상 걸릴 수 있다. 본선 1주 전 신청 마감 |
| 참가 제한 | 외국인 참가자는 데이터 신청이 불가하다. 공고에 명시 |

### B.5 확인 필요

- 88과 71299의 라이선스 유형(상업적 이용 가능 여부)
- 88의 실제 용량과 bbox 단위(글자/단어/줄)
- 71811의 행정문서 비중

---

## Part C. O3 조사 — 혼합 레이아웃(표·도면·수식) 파서 비교

### C.1 판정

PDF 확보는 쉽다. 정답 라벨이 없다. 특허 공보에는 레이아웃 정답이 없고, 제조 기술지침은 PDF 링크 접근성을 확인하지 못했다. 평가를 "정답 대조"에서 "파서 간 합의 + 사람 검수 + 하위 과제 정답"으로 바꾸면 실현 가능하다.

### C.2 후보 데이터

| 데이터 | 출처 | 접근 조건 | 정답 | 비고 |
|---|---|---|---|---|
| 특허 공개·등록공보 전문 | KIPRIS Plus API (data.go.kr 15065437) | 무료 월 1,000회, 개발단계 자동승인, XML로 전문·대표도면 다운로드 경로 제공 | 없음 | 표·도면·수식·청구항 혼합. 월 한도 내 500건 수준 |
| 단계적 사고 기반 특허 도면 추론 | AI Hub 71919 | 내국인, 승인 | 도면 PNG 4만 + 구성요소·관계·기능 CoT JSON | 도면 이해 하위 과제 정답 |
| 건축 도면 데이터 | AI Hub 71465 | 내국인, 승인 | 4.8만 장, 구조·공간·객체 bbox + OCR 문자 30만 | 도면 내 문자·객체 정답 |
| 수식·도형·낙서기호 OCR | AI Hub 479 | 내국인, 승인 | 미확인 | 수식 하위 과제 |
| 오피스 문서 생성 데이터 | AI Hub 71811 | 내국인, 승인 | 레이아웃 bbox + plain_text, 표 13,648개 | **혼합 레이아웃 정답이 있는 유일한 후보** |
| KOSHA GUIDE 기술지원규정 | 공공데이터포털 API 15144147 | 이용허락 제한 없음, JSON, 다운로드 링크 제공 | 없음 | 제조·안전 기술 문서. PDF 직접 접근 여부 미확인(페이지 로드 실패) |
| 학술논문 이해 데이터 | AI Hub 71845 | 내국인, 승인 | 미확인 | 수식·표·그림 혼합 가능성 |
| 특허 지식베이스 도면 태그 | AI Hub (2017) | 내국인, 승인 | 도면 번호·태그·추출 문자 이미지 | 오래됨. 전체 도면 이미지 아님 |

### C.3 해커톤 설계 제안

| 항목 | 제안 |
|---|---|
| 구조 | 2단 평가. 1단은 71811로 레이아웃 정답 대조(bbox IoU, 요소 분류 F1, 텍스트 CER). 2단은 특허 공보 PDF 300페이지로 분포 밖(OOD) 테스트 |
| OOD 정답 | 파서 5종 출력의 다수결을 가정답으로 두고, 불일치 페이지 200장을 사람이 검수해 최종 정답 제작. 검수 자체를 사전 준비 단계 과제로 |
| 도면 | 71919로 "도면에서 구성요소 번호와 명칭 추출" 하위 과제 추가. CoT 라벨이 있어 LLM-as-judge 설계 연습이 된다 |
| 제조 문서 | KOSHA GUIDE PDF 직접 링크가 확인되면 OOD 세트에 100페이지 추가. 확인 전까지는 제외 |
| 한도 | KIPRIS 월 1,000회는 주최 측이 사전 수집. 참가자 배포는 공보 PDF가 공개 자료라 가능하나 KIPRIS Plus 약관(원문 재배포)과 충돌 소지가 있어 담당자 사전 문의 |

### C.4 확인 필요

- KOSHA GUIDE 다운로드 링크가 로그인 없이 PDF를 주는지
- 특허 공보 PDF를 참가자에게 묶음으로 나눠줘도 되는지 (KIPRIS Plus 02-6915-1553)
- 479, 71845의 라벨 형식

---

## Part D. 종합 판정

| 주제 | 데이터 확보 | 정답 라벨 | 접근 비용 | 사전 준비 | 판정 |
|---|---|---|---|---|---|
| O1 DART | 확인 완료 | XBRL로 자동 | 0원 | 매핑표·평가 스크립트 2주 | **즉시 실행 가능** |
| O2 행정문서 | AI Hub 6종 확인 | 텍스트는 있음, 구조는 다른 데이터로 보강 | 0원 | 데이터 신청 1주 + 키-값 라벨 200장 | 실행 가능, 설계 조정 필요 |
| O3 혼합 레이아웃 | PDF 확보 쉬움 | 71811 외에는 없음 | 0원 | 가정답 제작 + 검수 2주 | 실행 가능, 평가 구조 변경 필요 |

우선순위는 O1, O2, O3 순이다. O1과 O2를 같은 해커톤의 두 트랙으로 두고, O3는 O1·O2 결과물이 쌓인 뒤 2회차 주제로 미루는 편이 안전하다.

---

## 부록. 출처

- [OpenDART 공시서류원본파일 API](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019003)
- [OpenDART 재무제표 원본파일(XBRL) API](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019019)
- [OpenDART 단일회사 전체 재무제표 API](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019020)
- [DART PDF 다운로드 페이지 예시](https://dart.fss.or.kr/pdf/download/main.do?rcp_no=20180330002076&dcm_no=6034949)
- [OpenDART 재무제표 API 사용 주의점 (2차 자료)](https://algolab.co.kr/blog/dart-opendart-financial-statement-api-lag-2026)
- [AI Hub 이용정책](https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105)
- [AI Hub 공공행정문서 OCR (88)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=88)
- [AI Hub OCR 데이터(공공) (71299)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71299)
- [AI Hub OCR 데이터(금융 및 물류) (71301)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71301)
- [AI Hub 금융업 특화 문서 OCR (632)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=632)
- [AI Hub 오피스 문서 생성 데이터 (71811)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71811)
- [AI Hub 표 이미지-텍스트 쌍 데이터 (71709)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71709)
- [AI Hub 단계적 사고 기반 특허 도면 추론 데이터 (71919)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71919)
- [AI Hub 건축 도면 데이터 (71465)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465)
- [AI Hub 특허 지식베이스](https://aihub.or.kr/aidata/30)
- [KIPRISPlus 특허·실용 공개·등록공보 REST API](https://www.data.go.kr/data/15065437/openapi.do?recommendDataYn=Y)
- [한국산업안전보건공단 기술지원규정(KOSHA GUIDE) 조회 API](https://www.data.go.kr/data/15144147/openapi.do)
- [PulseBench-Tab 다국어 표 추출 벤치마크](https://arxiv.org/pdf/2606.07534)
- [KoViDoRe (Upstage Document Parse 사용 사례)](https://arxiv.org/pdf/2608.20840)
