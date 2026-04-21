"""ChannelMonitor 테스트."""

import pytest
from src.community_manager.monitor import ChannelMonitor


@pytest.fixture
def monitor() -> ChannelMonitor:
    return ChannelMonitor()


def test_classify_question(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({"text": "이 기능은 어떻게 사용하나요?"}) == "question"


def test_classify_announcement(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({"text": "공지: 서비스 점검이 예정되어 있습니다."}) == "announcement"


def test_classify_spam(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({"text": "광고 무료 구독 지금 신청하세요"}) == "spam"


def test_classify_general(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({"text": "오늘 날씨가 좋네요."}) == "general"


def test_classify_empty_text(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({"text": ""}) == "general"


def test_classify_missing_text_key(monitor: ChannelMonitor) -> None:
    assert monitor.classify_message({}) == "general"


def test_get_summary_counts(monitor: ChannelMonitor) -> None:
    messages = [
        {"text": "공지사항입니다."},
        {"text": "어떻게 하면 되나요?"},
        {"text": "안녕하세요."},
        {"text": "광고 클릭하세요"},
    ]
    summary = monitor.get_summary(messages)
    assert summary["total"] == 4
    assert summary["announcement"] == 1
    assert summary["question"] == 1
    assert summary["general"] == 1
    assert summary["spam"] == 1


def test_get_summary_empty(monitor: ChannelMonitor) -> None:
    summary = monitor.get_summary([])
    assert summary["total"] == 0
    assert all(summary[k] == 0 for k in ("question", "announcement", "general", "spam"))
