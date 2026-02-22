# 실습용 샘플 데이터셋

이 폴더에는 가이드의 실습에서 사용할 수 있는 샘플 데이터가 포함되어 있습니다.
실제 데이터가 아닌 학습 목적으로 생성된 가상 데이터입니다.

## 파일 목록

| 파일 | 관련 챕터 | 설명 |
|------|----------|------|
| `user-survey-results.csv` | [4.1 유저 리서치](../4.1-discovery-user-research.md) | 30명 사용자 설문 데이터 (만족도, NPS, 기능 사용, 불만 사항) |
| `ab-test-results.csv` | [7.1 실험 분석](../7.1-growth-experiment-analysis.md) | 2주간 A/B 테스트 데이터 (방문자, 가입, 전환, 매출) |
| `competitor-data.json` | [4.2 경쟁사 분석](../4.2-discovery-competitive-analysis.md) | 경쟁사 3곳 구조화 데이터 (가격, 기능, 강점/약점, 시장) |

## 사용 방법

```bash
# Claude Code에서 바로 사용:
> @samples/user-survey-results.csv 이 설문 데이터를 분석해줘

# 또는 파일 지정:
> @samples/ab-test-results.csv 이 A/B 테스트 결과의 통계적 유의성을 검증해줘
```

---

> **© 2026 김생근 (Sanguine Kim)** | AI Agent Lead & AI Tutor
> 본 자료는 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 라이선스를 따릅니다.
> 교육·학술 목적 자유 이용 가능 | 상업적 이용 시 별도 라이선스 필요
> 강의·기업 교육·상업적 활용 문의: kimsanguine@gmail.com
