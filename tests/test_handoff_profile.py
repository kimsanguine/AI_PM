import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPOSITORY_ROOT / "scripts" / "validate_handoff_profile.py"
SCHEMA = REPOSITORY_ROOT / "contracts" / "ai-pm-handoff-profile-v0.schema.json"
FIXTURES = REPOSITORY_ROOT / "contracts" / "fixtures"
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
SCHEMA_FORMAT_CHECKER = FormatChecker()


@SCHEMA_FORMAT_CHECKER.checks("date-time", raises=(TypeError, ValueError))
def is_iso_date_time(value: object) -> bool:
    if not isinstance(value, str):
        return True
    datetime.fromisoformat(value)
    return True


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


def run_validator(fixture_name: str) -> subprocess.CompletedProcess[str]:
    return run_cli(str(FIXTURES / fixture_name))


def load_fixture(fixture_name: str) -> dict[str, Any]:
    with (FIXTURES / fixture_name).open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise AssertionError(f"fixture is not an object: {fixture_name}")
    return payload


def run_bytes(raw_json: bytes) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "profile.json"
        path.write_bytes(raw_json)
        return run_cli(str(path))


def run_raw(raw_json: str) -> subprocess.CompletedProcess[str]:
    return run_bytes(raw_json.encode("utf-8"))


def run_payload(payload: dict[str, Any]) -> subprocess.CompletedProcess[str]:
    return run_raw(json.dumps(payload))


class HandoffProfileValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with SCHEMA.open(encoding="utf-8") as handle:
            cls.schema = json.load(handle)
        Draft202012Validator.check_schema(cls.schema)
        cls.schema_validator = Draft202012Validator(
            cls.schema,
            format_checker=SCHEMA_FORMAT_CHECKER,
        )

    def assert_rejected(
        self,
        result: subprocess.CompletedProcess[str],
        field: str,
    ) -> None:
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        stderr_lines = result.stderr.splitlines()
        self.assertEqual(len(stderr_lines), 1)
        self.assertTrue(stderr_lines[0].strip())
        self.assertIn(field, stderr_lines[0])

    def assert_payload_rejected(
        self,
        payload: dict[str, Any],
        field: str,
    ) -> None:
        self.assertFalse(self.schema_validator.is_valid(payload))
        self.assert_rejected(run_payload(payload), field)

    def assert_fixture_rejected(self, fixture_name: str, field: str) -> None:
        payload = load_fixture(fixture_name)
        self.assertFalse(self.schema_validator.is_valid(payload))
        self.assert_rejected(run_validator(fixture_name), field)

    def test_schema_declares_draft_2020_12(self) -> None:
        self.assertEqual(
            self.schema.get("$schema"),
            "https://json-schema.org/draft/2020-12/schema",
        )

    def test_accepts_both_valid_public_fixtures(self) -> None:
        for fixture_name in (
            "hplan-build-gate-to-growth.valid.json",
            "growth-outcome-to-reconsideration.valid.json",
        ):
            with self.subTest(fixture=fixture_name):
                payload = load_fixture(fixture_name)
                result = run_validator(fixture_name)

                self.assertTrue(self.schema_validator.is_valid(payload))
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "")

    def test_rejects_growth_reconsideration_without_reopen_reason(self) -> None:
        self.assert_fixture_rejected(
            "growth-outcome-missing-reopen-reason.invalid.json",
            "reopen_reason",
        )

    def test_rejects_unknown_profile_version(self) -> None:
        self.assert_fixture_rejected(
            "unsupported-profile-version.invalid.json",
            "profile_version",
        )

    def test_rejects_unknown_field(self) -> None:
        payload = load_fixture("hplan-build-gate-to-growth.valid.json")
        payload["unexpected"] = True

        self.assert_payload_rejected(payload, "unexpected")

    def test_rejects_every_missing_required_field(self) -> None:
        base = load_fixture("hplan-build-gate-to-growth.valid.json")
        for field in REQUIRED_FIELDS:
            with self.subTest(field=field):
                payload = dict(base)
                del payload[field]

                self.assert_payload_rejected(payload, field)

    def test_rejects_unsupported_enum_values(self) -> None:
        base = load_fixture("hplan-build-gate-to-growth.valid.json")
        for field, value in (
            ("source_system", "other-system"),
            ("handoff_kind", "other_handoff"),
        ):
            with self.subTest(field=field):
                payload = dict(base)
                payload[field] = value

                self.assert_payload_rejected(payload, field)

    def test_rejects_invalid_utc_timestamps(self) -> None:
        base = load_fixture("hplan-build-gate-to-growth.valid.json")
        for review_at in (
            "2026-08-18 09:00:00Z",
            "2026-08-18T09:00:00+09:00",
            "2026-02-30T09:00:00Z",
        ):
            with self.subTest(review_at=review_at):
                payload = dict(base)
                payload["review_at"] = review_at

                self.assert_payload_rejected(payload, "review_at")

    def test_rejects_invalid_reference_fields(self) -> None:
        base = load_fixture("hplan-build-gate-to-growth.valid.json")
        for field, value in (
            ("source_record_ref", "CP-0001"),
            ("evidence_refs", ["EV-0001"]),
            ("metric_refs", "stg://metric/MET-0001"),
        ):
            with self.subTest(field=field):
                payload = dict(base)
                payload[field] = value

                self.assert_payload_rejected(payload, field)

    def test_rejects_whitespace_only_strings(self) -> None:
        base = load_fixture("hplan-build-gate-to-growth.valid.json")
        for field in ("project_id", "status", "owner"):
            with self.subTest(field=field):
                payload = dict(base)
                payload[field] = "   "

                self.assert_payload_rejected(payload, field)

        growth = load_fixture("growth-outcome-to-reconsideration.valid.json")
        growth["reopen_reason"] = "   "
        self.assert_payload_rejected(growth, "reopen_reason")

        build_gate = load_fixture("hplan-build-gate-to-growth.valid.json")
        build_gate["reopen_reason"] = "   "
        self.assert_payload_rejected(build_gate, "reopen_reason")

    def test_rejects_invalid_utf_8(self) -> None:
        self.assert_rejected(run_bytes(b'{"owner":"\xff"}'), "input")

    def test_rejects_malformed_non_object_and_unreadable_input(self) -> None:
        self.assertFalse(self.schema_validator.is_valid([]))
        cases = (
            (run_raw("{broken"), "input"),
            (run_raw("[]"), "input"),
            (run_validator("does-not-exist.json"), "input"),
        )
        for result, field in cases:
            with self.subTest(stderr=result.stderr):
                self.assert_rejected(result, field)

    def test_rejects_wrong_argument_count(self) -> None:
        fixture = str(FIXTURES / "hplan-build-gate-to-growth.valid.json")
        for arguments in ((), (fixture, fixture)):
            with self.subTest(argument_count=len(arguments)):
                self.assert_rejected(run_cli(*arguments), "input")

    def test_rejects_incompatible_source_and_handoff_kind(self) -> None:
        cases = (
            (
                "hplan-build-gate-to-growth.valid.json",
                "signal-to-growth",
            ),
            (
                "growth-outcome-to-reconsideration.valid.json",
                "hplan",
            ),
        )
        for fixture_name, source_system in cases:
            with self.subTest(
                fixture=fixture_name,
                source_system=source_system,
            ):
                payload = load_fixture(fixture_name)
                payload["source_system"] = source_system

                self.assert_payload_rejected(payload, "handoff_kind")

    def test_rejects_incompatible_source_record_namespace(self) -> None:
        cases = (
            (
                "hplan-build-gate-to-growth.valid.json",
                "stg://outcome/OUT-0001",
            ),
            (
                "growth-outcome-to-reconsideration.valid.json",
                "hplan://checkpoint/CP-0001",
            ),
        )
        for fixture_name, source_record_ref in cases:
            with self.subTest(
                fixture=fixture_name,
                source_record_ref=source_record_ref,
            ):
                payload = load_fixture(fixture_name)
                payload["source_record_ref"] = source_record_ref

                self.assert_payload_rejected(payload, "source_record_ref")


if __name__ == "__main__":
    unittest.main()
