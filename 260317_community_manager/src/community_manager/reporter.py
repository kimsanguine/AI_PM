"""ActivityReporter — 일간/주간 활동 리포트 생성."""

from __future__ import annotations

from .monitor import ChannelMonitor


class ActivityReporter:
    """메시지 데이터를 집계하여 활동 리포트를 생성한다."""

    def __init__(self) -> None:
        self._monitor = ChannelMonitor()

    def daily_report(self, messages: list[dict]) -> dict:
        """하루 메시지로 일간 리포트를 생성한다.

        Returns:
            {
                "total_messages": int,
                "by_type": {"question": int, "announcement": int, "general": int, "spam": int},
                "top_users": list[str],
            }
        """
        summary = self._monitor.get_summary(messages)
        by_type = {k: summary[k] for k in ("question", "announcement", "general", "spam")}

        user_counts: dict[str, int] = {}
        for msg in messages:
            user = msg.get("user", "unknown")
            user_counts[user] = user_counts.get(user, 0) + 1
        top_users = sorted(user_counts, key=lambda u: user_counts[u], reverse=True)[:3]

        return {
            "total_messages": summary["total"],
            "by_type": by_type,
            "top_users": top_users,
        }

    def weekly_report(self, days: list[list[dict]]) -> dict:
        """복수 일자 메시지 리스트로 주간 리포트를 생성한다.

        Args:
            days: 각 요소가 하루치 메시지 리스트인 리스트 (최대 7개).

        Returns:
            {
                "total_messages": int,
                "daily_totals": list[int],
                "by_type": {"question": int, "announcement": int, "general": int, "spam": int},
                "active_days": int,
            }
        """
        daily_totals: list[int] = []
        combined_by_type: dict[str, int] = {"question": 0, "announcement": 0, "general": 0, "spam": 0}

        for day_messages in days:
            report = self.daily_report(day_messages)
            daily_totals.append(report["total_messages"])
            for key in combined_by_type:
                combined_by_type[key] += report["by_type"][key]

        return {
            "total_messages": sum(daily_totals),
            "daily_totals": daily_totals,
            "by_type": combined_by_type,
            "active_days": sum(1 for t in daily_totals if t > 0),
        }
