# PM 템플릿 & 커맨드 패키지

이 폴더에는 바로 복사해서 사용할 수 있는 템플릿과 슬래시 커맨드 예제가 포함되어 있습니다.

## CLAUDE.md 스타터 템플릿

| 파일 | 설명 |
|------|------|
| `CLAUDE-md-starter.md` | 프로젝트 루트에 CLAUDE.md로 복사하여 사용. PM 워크스페이스 설정, HITL 규칙, 분석 규칙, 프레임워크 포함 |

### 사용법
```bash
# 프로젝트 루트에 복사:
cp templates/CLAUDE-md-starter.md ./CLAUDE.md

# [괄호] 안의 내용을 자신의 정보로 교체
```

## 슬래시 커맨드 예제

| 파일 | 커맨드 | 관련 챕터 | 설명 |
|------|--------|----------|------|
| `commands/today.md` | `/today` | [3.3 슬래시 커맨드](../3.3-slash-commands.md) | 오늘의 PM 브리핑 자동 생성 |
| `commands/prd.md` | `/prd [기능명]` | [5.1 PRD 작성](../5.1-definition-write-prd.md) | 소크라틱 대화 기반 PRD 초안 생성 |
| `commands/status.md` | `/status` | [A.5 상태 보고서](../A.5-usecase-status-report.md) | 주간 상태 보고서 자동 생성 |

### 설치법
```bash
# .claude/commands/ 폴더로 복사:
mkdir -p .claude/commands
cp templates/commands/*.md .claude/commands/

# Claude Code에서 사용:
> /today
> /prd 온보딩 개선
> /status
```

---

> **© 2026 김생근 (Sanguine Kim)** | AI Agent Lead & AI Tutor
> 본 자료는 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 라이선스를 따릅니다.
> 교육·학술 목적 자유 이용 가능 | 상업적 이용 시 별도 라이선스 필요
> 강의·기업 교육·상업적 활용 문의: kimsanguine@gmail.com
