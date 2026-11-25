# 루틴팩 v1

완성된 규칙 모음이 아닙니다. [Harness Engineering Playbook](https://habix.ai/playbook/harness-engineering)에서 매일 쓰라고 한 파일 5종을, 내 프로젝트에 맞춰 채워 쓰는 빈칸 양식으로 묶은 것입니다.

`CLAUDE.md` 3종 변형 + `feature_list.json` + `progress.md` + `intent_sheet.md` + 세션 종료 체크리스트. 5종은 함께 작동하도록 설계되었습니다. 한두 개만 쓰면 예전처럼 헤매는 자리로 돌아갑니다.

## 5종과 각 파일이 하는 일

| # | 파일 | 하는 일 | 원문 |
|---|---|---|---|
| 1 | `CLAUDE.pm.md`, `CLAUDE.solo-builder.md`, `CLAUDE.marketer.md` | 프로젝트의 첫 페이지. AI가 세션마다 먼저 읽는 8칸 안내문. 페르소나별 3종 변형 중 하나만 골라 `CLAUDE.md`로 씁니다 | [챕터 4](https://habix.ai/playbook/harness-engineering/ch04-claude-md-one-page) |
| 2 | `feature_list.json` | 살아 있는 작업 5~10개의 뼈대. 항목마다 `id`, `behavior`, `verification`, `state` 4칸. `state`는 검증이 통과해야만 `passing` | [챕터 8](https://habix.ai/playbook/harness-engineering/ch08-feature-list-changes-everything) |
| 3 | `progress.md` | 매일 5칸. 어제와 오늘을 잇는 다리. 마지막 칸이 내일의 첫 명령 | [챕터 5](https://habix.ai/playbook/harness-engineering/ch05-leave-notes-for-tomorrow) |
| 4 | `intent_sheet.md` | 의도, 결과 정의, 제약, 정지 규칙, 평가 지표, 휴먼 체크포인트를 한 장에. AI에게 시키기 전에 채웁니다 | [챕터 7](https://habix.ai/playbook/harness-engineering/ch07-stop-ai-from-overreaching) |
| 5 | `session-end-checklist.md` | 매 세션 마지막 5분의 의식. 10가지 확인 | [챕터 12](https://habix.ai/playbook/harness-engineering/ch12-clean-exit) |

`feature_list.json`의 `state`는 `todo` / `active` / `passing` / `failing` / `blocked` 중 하나입니다. `owner`와 `notes`는 익숙해진 후에 채워도 됩니다. 처음 시작할 때는 빈 `[]` 한 줄로 두고 예시 항목을 지워도 됩니다.

## 페르소나별 고르는 법

`CLAUDE.md` 변형은 본인 페르소나 한 줄에 맞춰 한 가지만 고릅니다. 나머지 4종은 모두 공통입니다.

| 페르소나 | 고를 파일 | 미리 막는 사고 |
|---|---|---|
| PM | `CLAUDE.pm.md` (변형 A) | 회의록 원본 덮어쓰기, 요약본에 고객사명과 매출 수치 노출 |
| 1인 빌더 | `CLAUDE.solo-builder.md` (변형 B) | Lovable 생성 파일 일괄 리팩토링, main 직접 푸시, Stripe 라이브 키 노출 |
| 마케터 | `CLAUDE.marketer.md` (변형 C) | 사람 검토 없는 자동 발행, 채널마다 같은 문장 복붙 |

## 복사

이 저장소 루트에서 실행합니다. `P`는 내 프로젝트 폴더로 바꾸세요.

```bash
P=~/my-ai-workshop
mkdir -p "$P"

# CLAUDE.md는 변형 하나만 골라 이름을 바꿔 복사합니다 (pm, solo-builder, marketer 중 하나)
cp templates/routine-pack-v1/CLAUDE.pm.md "$P/CLAUDE.md"

# 나머지 4종은 그대로 복사합니다
cp templates/routine-pack-v1/feature_list.json \
   templates/routine-pack-v1/progress.md \
   templates/routine-pack-v1/intent_sheet.md \
   templates/routine-pack-v1/session-end-checklist.md "$P/"
```


## 하루에 쓰는 순서

1. 작업 하나를 시키기 전에 `intent_sheet.md`를 채웁니다. ([챕터 7](https://habix.ai/playbook/harness-engineering/ch07-stop-ai-from-overreaching))
2. 새 세션을 열면 `CLAUDE.md`, `progress.md`, `feature_list.json` 순서로 한 문서씩 읽힙니다. ([챕터 6](https://habix.ai/playbook/harness-engineering/ch06-five-minute-briefing))
3. 작업 중에는 `feature_list.json`의 `state`를 검증 결과로만 바꿉니다. ([챕터 8](https://habix.ai/playbook/harness-engineering/ch08-feature-list-changes-everything))
4. 세션을 닫기 5분 전에 `progress.md` 5칸을 채우고 `session-end-checklist.md`를 훑습니다. ([챕터 5](https://habix.ai/playbook/harness-engineering/ch05-leave-notes-for-tomorrow), [챕터 12](https://habix.ai/playbook/harness-engineering/ch12-clean-exit))

30일 동안 이 순서를 굴리는 방법은 [Capstone](https://habix.ai/playbook/harness-engineering/capstone-30-day-routine-challenge)에, 한 달 후 이 파일들을 정리하는 방법은 [챕터 13](https://habix.ai/playbook/harness-engineering/ch13-refactor-your-routine-files)에 있습니다.

## 원문

- [Harness Engineering Playbook 허브](https://habix.ai/playbook/harness-engineering)
- [챕터 2. 하네스란, AI에게 일 시키는 작업장 차리기](https://habix.ai/playbook/harness-engineering/ch02-set-up-the-workshop)
- [챕터 4. CLAUDE.md 한 장으로 AI에게 우리 프로젝트 가르치기](https://habix.ai/playbook/harness-engineering/ch04-claude-md-one-page)
- [챕터 5. AI는 어제 한 일을 잊는다, 메모를 남겨라](https://habix.ai/playbook/harness-engineering/ch05-leave-notes-for-tomorrow)
- [챕터 7. AI가 일 키우는 걸 막는 법](https://habix.ai/playbook/harness-engineering/ch07-stop-ai-from-overreaching)
- [챕터 8. 할 일 한 장이 모든 것을 바꾼다](https://habix.ai/playbook/harness-engineering/ch08-feature-list-changes-everything)
- [챕터 12. 내일의 나를 위해 책상 정리하고 나가기](https://habix.ai/playbook/harness-engineering/ch12-clean-exit)
