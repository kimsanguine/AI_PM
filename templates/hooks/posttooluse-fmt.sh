#!/usr/bin/env bash
#
# PostToolUse hook — Edit / Write 도구로 파일이 수정된 직후 포매터·린터를 자동 실행.
# 검증 사다리 1단(자동 포맷)을 매 편집마다 강제하는 폐루프.
#
# 설치:
#   1. 이 파일을 ~/.claude/hooks/posttooluse-fmt.sh 로 복사
#   2. chmod +x ~/.claude/hooks/posttooluse-fmt.sh
#   3. ~/.claude/settings.json 에 등록:
#        {
#          "hooks": {
#            "PostToolUse": [{
#              "matcher": { "tool_name": ["Edit", "Write"] },
#              "command": "~/.claude/hooks/posttooluse-fmt.sh"
#            }]
#          }
#        }
#
# 환경 변수 CLAUDE_TOOL_RESULT_PATH 또는 stdin 으로 편집된 파일 경로를 받는 것을 가정.

set -euo pipefail

# Claude Code 가 어떤 파일을 수정했는지 — stdin 으로 JSON 받기
INPUT="$(cat || true)"
FILE_PATH="$(printf '%s' "$INPUT" | grep -oE '"file_path"\s*:\s*"[^"]+"' | head -1 | sed -E 's/.*"file_path"\s*:\s*"([^"]+)".*/\1/' || true)"

if [[ -z "${FILE_PATH:-}" ]]; then
  exit 0
fi

case "$FILE_PATH" in
  *.py)
    command -v ruff >/dev/null 2>&1 && ruff format "$FILE_PATH" 2>/dev/null || true
    command -v ruff >/dev/null 2>&1 && ruff check --fix "$FILE_PATH" 2>/dev/null || true
    ;;
  *.ts|*.tsx|*.js|*.jsx|*.json|*.md)
    command -v prettier >/dev/null 2>&1 && prettier --write "$FILE_PATH" 2>/dev/null || true
    ;;
  *.sh)
    command -v shfmt >/dev/null 2>&1 && shfmt -w "$FILE_PATH" 2>/dev/null || true
    ;;
esac
