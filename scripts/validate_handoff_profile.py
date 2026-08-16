#!/usr/bin/env python3
"""Validate an AI PM Handoff Profile v0 JSON envelope."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "profile_version",
    "project_id",
    "source_system",
    "source_record_ref",
    "handoff_kind",
    "status",
    "evidence_refs",
    "metric_refs",
    "owner",
    "review_at",
)
ALLOWED_FIELDS = set(REQUIRED_FIELDS) | {"reopen_reason"}
SOURCE_SYSTEMS = {"hplan", "signal-to-growth"}
HANDOFF_SOURCE_SYSTEM = {
    "build_gate_to_growth": "hplan",
    "growth_outcome_to_reconsideration": "signal-to-growth",
}
HANDOFF_KINDS = set(HANDOFF_SOURCE_SYSTEM)
SOURCE_RECORD_PREFIX = {
    "hplan": "hplan://",
    "signal-to-growth": "stg://",
}
REFERENCE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://\S+$")
UTC_RFC3339_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|\+00:00)$"
)


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_reference(field: str, value: Any) -> str | None:
    if not _non_empty_string(value) or REFERENCE_PATTERN.fullmatch(value) is None:
        return f"{field}: expected an opaque URI reference"
    return None


def _validate_reference_list(field: str, value: Any) -> str | None:
    if not isinstance(value, list):
        return f"{field}: expected an array of opaque URI references"
    for item in value:
        if _validate_reference(field, item) is not None:
            return f"{field}: expected an array of opaque URI references"
    return None


def _validate_review_at(value: Any) -> str | None:
    if not isinstance(value, str) or UTC_RFC3339_PATTERN.fullmatch(value) is None:
        return "review_at: expected a UTC RFC 3339 timestamp"
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return "review_at: expected a UTC RFC 3339 timestamp"
    if parsed.utcoffset() != timedelta(0):
        return "review_at: expected a UTC RFC 3339 timestamp"
    return None


def validate_profile(profile: dict[str, Any]) -> str | None:
    """Return the first field-specific validation error, or ``None``."""
    unknown_fields = sorted(set(profile) - ALLOWED_FIELDS)
    if unknown_fields:
        return f"{unknown_fields[0]}: unknown field"

    for field in REQUIRED_FIELDS:
        if field not in profile:
            return f"{field}: required field is missing"

    if profile["profile_version"] != "0.1":
        return "profile_version: unsupported value"
    if not _non_empty_string(profile["project_id"]):
        return "project_id: expected a non-empty string"
    if (
        not isinstance(profile["source_system"], str)
        or profile["source_system"] not in SOURCE_SYSTEMS
    ):
        return "source_system: unsupported value"

    error = _validate_reference("source_record_ref", profile["source_record_ref"])
    if error:
        return error

    if (
        not isinstance(profile["handoff_kind"], str)
        or profile["handoff_kind"] not in HANDOFF_KINDS
    ):
        return "handoff_kind: unsupported value"
    expected_source = HANDOFF_SOURCE_SYSTEM[profile["handoff_kind"]]
    if expected_source != profile["source_system"]:
        return "handoff_kind: incompatible with source_system"
    if not profile["source_record_ref"].startswith(
        SOURCE_RECORD_PREFIX[profile["source_system"]]
    ):
        return "source_record_ref: incompatible with source_system namespace"
    if not _non_empty_string(profile["status"]):
        return "status: expected a non-empty string"

    for field in ("evidence_refs", "metric_refs"):
        error = _validate_reference_list(field, profile[field])
        if error:
            return error

    if not _non_empty_string(profile["owner"]):
        return "owner: expected a non-empty string"

    error = _validate_review_at(profile["review_at"])
    if error:
        return error

    if profile["handoff_kind"] == "growth_outcome_to_reconsideration":
        if not _non_empty_string(profile.get("reopen_reason")):
            return "reopen_reason: required for growth outcome reconsideration"
    elif "reopen_reason" in profile and not _non_empty_string(
        profile["reopen_reason"]
    ):
        return "reopen_reason: expected a non-empty string"

    return None


def _load_profile(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        with path.open(encoding="utf-8") as handle:
            value = json.load(handle)
    except OSError as exc:
        return None, f"input: unable to read JSON file ({exc})"
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, f"input: malformed UTF-8 JSON ({exc})"

    if not isinstance(value, dict):
        return None, "input: expected a JSON object"
    return value, None


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("input: expected exactly one JSON file", file=sys.stderr)
        return 1

    profile, error = _load_profile(Path(argv[0]))
    if error is None and profile is not None:
        error = validate_profile(profile)
    if error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
