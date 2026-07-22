from collections import defaultdict

from app.history.run_history import RunHistory
from app.storage.run_repository import RunRepository


class LeaderboardService:

    def list(self):

        history = RunHistory().load()

        rows = defaultdict(
            lambda: {
                "model": "",
                "accuracy": 0,
                "latency_ms": 0,
                "tokens": 0,
                "cost": 0,
                "runs": 0,
            }
        )

        repo = RunRepository()

        for summary in history:

            run = repo.load(summary.path)

            if run is None:
                continue

            for exp in run.experiments:

                key = exp.model.name

                row = rows[key]

                row["model"] = exp.model.name
                row["accuracy"] += exp.accuracy
                row["latency_ms"] += exp.average_latency
                row["tokens"] += exp.average_total_tokens
                row["cost"] += exp.cost.total_cost
                row["runs"] += 1

        leaderboard = []

        for row in rows.values():

            runs = row["runs"]

            leaderboard.append(
                {
                    "model": row["model"],
                    "accuracy": row["accuracy"] / runs,
                    "latency_ms": row["latency_ms"] / runs,
                    "tokens": int(row["tokens"]),
                    "cost": row["cost"],
                    "runs": runs,
                }
            )

        leaderboard.sort(
            key=lambda x: x["accuracy"],
            reverse=True,
        )

        return leaderboard
