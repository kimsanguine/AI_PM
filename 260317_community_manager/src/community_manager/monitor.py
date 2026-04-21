"""ChannelMonitor — 메시지 스트림 분류 및 요약."""

from __future__ import annotations

_QUESTION_KEYWORDS = ("?", "어떻게", "무엇", "어디", "언제", "왜", "방법", "알려", "알고 싶")
_ANNOUNCEMENT_KEYWORDS = ("공지", "안내", "업데이트", "릴리즈", "출시", "발표", "notice", "announce", "update")
_SPAM_KEYWORDS = ("광고", "홍보", "무료 구독", "클릭", "spam", "promo", "free money", "click here")

MessageType = str  # "question" | "announcement" | "general" | "spam"


class ChannelMonitor:
    """채널 메시지를 분류하고 통계를 집계한다."""

    def classify_message(self, msg: dict) -> MessageType:
        """단일 메시지를 분류한다.

        Args:
            msg: {"text": str, ...} 형태의 메시지 dict.

        Returns:
            "question" | "announcement" | "general" | "spam"
        """
        text: str = msg.get("text", "").lower()

        if any(kw in text for kw in _SPAM_KEYWORDS):
            return "spam"
        if any(kw in text for kw in _ANNOUNCEMENT_KEYWORDS):
            return "announcement"
        if any(kw in text for kw in _QUESTION_KEYWORDS):
            return "question"
        return "general"

    def get_summary(self, messages: list[dict]) -> dict:
        """메시지 리스트를 분류하고 유형별 카운트를 반환한다.

        Returns:
            {
                "total": int,
                "question": int,
                "announcement": int,
                "general": int,
                "spam": int,
            }
        """
        counts: dict[str, int] = {"question": 0, "announcement": 0, "general": 0, "spam": 0}
        for msg in messages:
            msg_type = self.classify_message(msg)
            counts[msg_type] += 1
        return {"total": len(messages), **counts}
