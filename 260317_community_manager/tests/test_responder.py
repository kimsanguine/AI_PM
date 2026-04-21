"""AutoResponder 테스트."""

import pytest
from src.community_manager.responder import AutoResponder

FAQ_DB: list[dict] = [
    {"keywords": ["가격", "요금"], "answer": "요금 페이지를 확인하세요."},
    {"keywords": ["환불", "refund"], "answer": "환불은 7일 이내 가능합니다."},
    {"keywords": ["가입", "회원"], "answer": "회원가입 버튼을 클릭하세요."},
]


@pytest.fixture
def responder() -> AutoResponder:
    return AutoResponder()


def test_match_faq_korean_keyword(responder: AutoResponder) -> None:
    result = responder.match_faq("요금이 얼마인가요?", FAQ_DB)
    assert result is not None
    assert "요금" in result["keywords"]


def test_match_faq_english_keyword(responder: AutoResponder) -> None:
    result = responder.match_faq("I want a refund", FAQ_DB)
    assert result is not None
    assert result["answer"] == "환불은 7일 이내 가능합니다."


def test_match_faq_no_match(responder: AutoResponder) -> None:
    result = responder.match_faq("오늘 날씨 어때요?", FAQ_DB)
    assert result is None


def test_match_faq_empty_db(responder: AutoResponder) -> None:
    result = responder.match_faq("가격이 궁금해요", [])
    assert result is None


def test_match_faq_case_insensitive(responder: AutoResponder) -> None:
    result = responder.match_faq("REFUND please", FAQ_DB)
    assert result is not None


def test_onboard_message_contains_username(responder: AutoResponder) -> None:
    msg = responder.onboard_message("Alice")
    assert "Alice" in msg


def test_onboard_message_is_string(responder: AutoResponder) -> None:
    msg = responder.onboard_message("Bob")
    assert isinstance(msg, str)
    assert len(msg) > 0
