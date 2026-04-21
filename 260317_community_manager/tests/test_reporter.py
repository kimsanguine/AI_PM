"""ActivityReporter 테스트."""

import pytest
from src.community_manager.reporter import ActivityReporter


@pytest.fixture
def reporter() -> ActivityReporter:
    return ActivityReporter()


SAMPLE_MESSAGES: list[dict] = [
    {"text": "공지: 업데이트 안내입니다.", "user": "admin"},
    {"text": "어떻게 사용하나요?", "user": "alice"},
    {"text": "광고 클릭하세요", "user": "spammer"},
    {"text": "안녕하세요.", "user": "alice"},
    {"text": "감사합니다.", "user": "bob"},
]


def test_daily_report_total(reporter: ActivityReporter) -> None:
    report = reporter.daily_report(SAMPLE_MESSAGES)
    assert report["total_messages"] == len(SAMPLE_MESSAGES)


def test_daily_report_by_type_keys(reporter: ActivityReporter) -> None:
    report = reporter.daily_report(SAMPLE_MESSAGES)
    assert set(report["by_type"].keys()) == {"question", "announcement", "general", "spam"}


def test_daily_report_top_users(reporter: ActivityReporter) -> None:
    report = reporter.daily_report(SAMPLE_MESSAGES)
    assert "alice" in report["top_users"]


def test_daily_report_empty(reporter: ActivityReporter) -> None:
    report = reporter.daily_report([])
    assert report["total_messages"] == 0
    assert report["top_users"] == []


def test_weekly_report_total(reporter: ActivityReporter) -> None:
    days = [SAMPLE_MESSAGES, SAMPLE_MESSAGES, []]
    report = reporter.weekly_report(days)
    assert report["total_messages"] == len(SAMPLE_MESSAGES) * 2


def test_weekly_report_active_days(reporter: ActivityReporter) -> None:
    days = [SAMPLE_MESSAGES, [], SAMPLE_MESSAGES]
    report = reporter.weekly_report(days)
    assert report["active_days"] == 2


def test_weekly_report_daily_totals_length(reporter: ActivityReporter) -> None:
    days = [SAMPLE_MESSAGES] * 7
    report = reporter.weekly_report(days)
    assert len(report["daily_totals"]) == 7


def test_weekly_report_empty(reporter: ActivityReporter) -> None:
    report = reporter.weekly_report([])
    assert report["total_messages"] == 0
    assert report["active_days"] == 0
