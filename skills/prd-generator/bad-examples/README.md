# bad-examples/

PM이 거부하거나 대폭 수정한 PRD가 저장되는 폴더입니다.

## 저장 규칙
- 파일명: `YYYYMMDD_[project-name]-prd-rejected.md`
- 파일 상단에 거부 사유를 기록:

```markdown
---
rejected: true
reason: "솔루션이 문제 정의와 맞지 않음. 기술 복잡성 과소평가."
date: YYYY-MM-DD
---
```

## 목적
- 같은 실수를 반복하지 않기 위한 학습 데이터
- Rules 섹션 업데이트의 근거
- "왜 이 PRD가 좋지 않았는가"를 명시적으로 기록
