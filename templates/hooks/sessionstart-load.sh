#!/usr/bin/env bash
#
# SessionStart hook — Claude Code 세션이 시작될 때 INDEX.md 와 README 의 첫 단락을
# 컨텍스트로 주입한다. 모델이 작업 전 "이 레포가 무엇이고 무엇이 어디에 있는지" 를
# 매번 자동으로 알게 한다.
#
# 설치:
#   1. 이 파일을 ~/.claude/hooks/sessionstart-load.sh 로 복사
#   2. chmod +x ~/.claude/hooks/sessionstart-load.sh
#   3. ~/.claude/settings.json 에 등록:
#        {
#          "hooks": {
#            "SessionStart": [{ "command": "~/.claude/hooks/sessionstart-load.sh" }]
#          }
#        }
#
# 출력은 모델에게 시스템 컨텍스트로 주입된다.

set -euo pipefail

echo "=== Repo entrypoint =================================="
echo "Working dir: $PWD"
echo ""

if [[ -f "INDEX.md" ]]; then
  echo "--- INDEX.md (지식 지도) ---"
  head -80 INDEX.md
  echo ""
fi

if [[ -f "CLAUDE.md" ]]; then
  echo "--- CLAUDE.md (행동 규칙 요약) ---"
  head -40 CLAUDE.md
  echo ""
fi

echo "=== End entrypoint ==================================="
