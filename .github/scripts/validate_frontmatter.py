#!/usr/bin/env python3
"""
챕터 md 파일들의 front-matter 스키마 검증.

현재 본 레포의 챕터들 대부분은 front-matter 가 아직 없음(v1.2 에서 일괄 추가 예정).
따라서 본 스크립트는 front-matter 가 존재하는 파일에 한해 스키마를 검증한다.

front-matter 가 있는 파일은 다음을 만족해야 한다:
  - YAML parse OK
  - 필수 키: chapter, last_updated
  - 권장 키: claude_model (값은 claude-opus-4-7 형식), claude_code_version
  - chapter 는 "X.Y" 또는 "A.N" 패턴
  - last_updated 는 YYYY-MM-DD
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

CHAPTER_RE = re.compile(r"^(?:\d+\.\d+(?:\.\d+)?|[A-Z]\.\d+)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MODEL_RE = re.compile(r"^claude-[a-z]+-\d+-\d+$")


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    try:
        return yaml.safe_load(block)
    except yaml.YAMLError:
        return {"_parse_error": True}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None:
        return errors  # front-matter 미존재 — 통과 (v1.2 까지 허용)
    if fm.get("_parse_error"):
        errors.append(f"{path}: YAML parse error in front-matter")
        return errors
    if "chapter" not in fm:
        errors.append(f"{path}: missing 'chapter' key")
    elif not CHAPTER_RE.match(str(fm["chapter"])):
        errors.append(f"{path}: chapter must match 'X.Y' or 'A.N' (got {fm['chapter']!r})")
    if "last_updated" not in fm:
        errors.append(f"{path}: missing 'last_updated' key")
    elif not DATE_RE.match(str(fm["last_updated"])):
        errors.append(f"{path}: last_updated must be YYYY-MM-DD (got {fm['last_updated']!r})")
    if "claude_model" in fm and not MODEL_RE.match(str(fm["claude_model"])):
        errors.append(f"{path}: claude_model must match 'claude-X-N-N' (got {fm['claude_model']!r})")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    targets = [p for p in root.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts]
    errors: list[str] = []
    for path in targets:
        errors.extend(validate(path))
    if errors:
        for err in errors:
            print(f"::error::{err}")
        return 1
    print(f"✓ front-matter validation OK ({len(targets)} files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
