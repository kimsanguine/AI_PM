"""AutoResponder — FAQ 자동 응답 및 온보딩 메시지 생성."""

from __future__ import annotations


class AutoResponder:
    """FAQ 키워드 매칭 및 온보딩 메시지를 처리한다."""

    def match_faq(self, text: str, faq_db: list[dict]) -> dict | None:
        """텍스트에 매칭되는 FAQ 항목을 반환한다.

        Args:
            text: 사용자 메시지 텍스트.
            faq_db: [{"keywords": list[str], "answer": str, ...}] 형태의 FAQ 목록.

        Returns:
            첫 번째 매칭 FAQ dict 또는 None.
        """
        lower_text = text.lower()
        for faq in faq_db:
            keywords: list[str] = faq.get("keywords", [])
            if any(kw.lower() in lower_text for kw in keywords):
                return faq
        return None

    def onboard_message(self, username: str) -> str:
        """신규 멤버 온보딩 환영 메시지를 생성한다.

        Args:
            username: 새로 합류한 멤버 이름.

        Returns:
            환영 메시지 문자열.
        """
        return (
            f"안녕하세요, {username}님! 커뮤니티에 오신 것을 환영합니다. "
            "궁금한 점이 있으시면 언제든지 질문해 주세요."
        )
