#!/usr/bin/env bash
#
# Stop hook — Claude Code 세션이 종료될 때 소리/알림으로 통보.
# 병렬 세션(3~6개) 운영 시 어느 세션이 끝났는지 즉시 알 수 있게 한다.
#
# 설치:
#   1. 이 파일을 ~/.claude/hooks/stop-notify.sh 로 복사
#   2. chmod +x ~/.claude/hooks/stop-notify.sh
#   3. ~/.claude/settings.json 에 등록:
#        {
#          "hooks": {
#            "Stop": [{ "command": "~/.claude/hooks/stop-notify.sh" }]
#          }
#        }

set -euo pipefail

# 세션 식별 — 현재 디렉토리 이름을 라벨로
SESSION_LABEL="$(basename "$PWD")"
MSG="Claude Code 세션 완료: ${SESSION_LABEL}"

# macOS — say + 시스템 사운드
if [[ "$(uname)" == "Darwin" ]]; then
  afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true
  osascript -e "display notification \"${MSG}\" with title \"Claude Code\"" 2>/dev/null || true
  exit 0
fi

# Linux — paplay + notify-send
if command -v paplay >/dev/null 2>&1; then
  paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || true
fi
if command -v notify-send >/dev/null 2>&1; then
  notify-send "Claude Code" "${MSG}" 2>/dev/null || true
fi

# Fallback — 터미널 벨
printf '\a'
