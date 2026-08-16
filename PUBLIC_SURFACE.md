# AI_PM Public Surface

AI_PM은 공개 교육용 저장소다. 기존 과정 자료와 사용자용 운영 가이드는 의도적인
공개 예외로 유지한다.

## 공개 범위

- `docs/part*/`, `docs/appendix/` — PM 학습 과정
- `docs/operations/` — 사용자가 실행·검토할 운영 가이드
- `README.md`, `INDEX.md`, `contracts/`, `scripts/`, `tests/`, `skills/`,
  `templates/` — 공개 학습·검증 surface

## 비공개 범위

- 내부 설계·작업 계획·에이전트 실행 기록은 Git에 두지 않는다.
- 포트폴리오 내부 설계·계획은 Git 밖의 로컬 `PrivateArchives/`에만 보관한다.

이 구분은 `docs/` 전체를 일괄 금지하는 정책이 아니다. 공개 과정 문서와
사용자용 운영 문서는 유지하되, 내부 planning artifact는 public branch에
commit하거나 push하지 않는다.
