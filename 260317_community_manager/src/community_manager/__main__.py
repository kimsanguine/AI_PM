"""CLI 진입점 — python -m community_manager."""

from __future__ import annotations

import argparse
import json
import sys

from . import ActivityReporter, AutoResponder, ChannelMonitor

SAMPLE_FAQ: list[dict] = [
    {"keywords": ["가격", "요금", "price"], "answer": "요금 안내 페이지를 확인해 주세요: https://example.com/pricing"},
    {"keywords": ["가입", "회원", "register", "signup"], "answer": "상단 메뉴의 '회원가입' 버튼을 클릭해 주세요."},
    {"keywords": ["환불", "refund"], "answer": "환불은 구매 후 7일 이내 가능합니다. 고객센터에 문의해 주세요."},
]


def cmd_classify(args: argparse.Namespace) -> None:
    monitor = ChannelMonitor()
    msg_type = monitor.classify_message({"text": args.text})
    print(f"분류 결과: {msg_type}")


def cmd_onboard(args: argparse.Namespace) -> None:
    responder = AutoResponder()
    print(responder.onboard_message(args.username))


def cmd_faq(args: argparse.Namespace) -> None:
    responder = AutoResponder()
    result = responder.match_faq(args.text, SAMPLE_FAQ)
    if result:
        print(f"FAQ 답변: {result['answer']}")
    else:
        print("매칭된 FAQ 없음")


def cmd_report(args: argparse.Namespace) -> None:
    messages = json.loads(args.messages)
    reporter = ActivityReporter()
    report = reporter.daily_report(messages)
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="community_manager",
        description="Community Manager CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_classify = sub.add_parser("classify", help="메시지 분류")
    p_classify.add_argument("text", help="분류할 메시지 텍스트")
    p_classify.set_defaults(func=cmd_classify)

    p_onboard = sub.add_parser("onboard", help="온보딩 메시지 생성")
    p_onboard.add_argument("username", help="신규 멤버 이름")
    p_onboard.set_defaults(func=cmd_onboard)

    p_faq = sub.add_parser("faq", help="FAQ 매칭")
    p_faq.add_argument("text", help="질문 텍스트")
    p_faq.set_defaults(func=cmd_faq)

    p_report = sub.add_parser("report", help="일간 리포트 생성")
    p_report.add_argument("messages", help='JSON 형태의 메시지 배열 (예: \'[{"text":"hi","user":"alice"}]\')')
    p_report.set_defaults(func=cmd_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
