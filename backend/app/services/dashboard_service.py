from pathlib import Path

from app.history.run_history import RunHistory
from app.services.run_status_service import RunStatusService
from app.storage.run_repository import RunRepository
from app.prompts import prompts
from app.model_registry import models


class DashboardService:

    def get(self):

        history = RunHistory().load()

        run_repository = RunRepository()

        total_experiments = 0
        total_cost = 0.0

        recent_runs = []
        leaderboard = []
        accuracy_trend = []

        # latest first
        for item in history:

            try:
                run = run_repository.load(item.path)
            except Exception:
                continue

            total_experiments += len(run.experiments)

            recent_runs.append(
                {
                    "id": run.id,
                    "name": Path(item.path).name,
                    "created_at": run.created_at.isoformat(),
                    "experiments": len(run.experiments),
                }
            )

            for exp in run.experiments:

                accuracy = 0

                if exp.results:
                    accuracy = (
                        sum(r.score for r in exp.results)
                        / len(exp.results)
                    )

                avg_latency = 0

                if exp.results:
                    avg_latency = (
                        sum(r.latency_ms for r in exp.results)
                        / len(exp.results)
                    )

                avg_tokens = 0

                if exp.results:
                    avg_tokens = (
                        sum(r.total_tokens for r in exp.results)
                        / len(exp.results)
                    )

                leaderboard.append(
                    {
                        "model": exp.model.name,
                        "prompt": exp.prompt.name,
                        "accuracy": accuracy,
                        "latency_ms": avg_latency,
                    }
                )

                accuracy_trend.append(
                    {
                        "run": Path(item.path).name,
                        "model": exp.model.name,
                        "prompt": exp.prompt.name,
                        "accuracy": accuracy,
                        "latency_ms": avg_latency,
                        "tokens": avg_tokens,
                    }
                )

        leaderboard.sort(
            key=lambda x: x["accuracy"],
            reverse=True,
        )

        statuses = RunStatusService().all()

        active = next(
            (
                s
                for s in statuses
                if s.status == "running"
            ),
            None,
        )

        return {
            "stats": {
                "runs": len(history),
                "datasets": len(
                    list(Path("datasets").glob("*.json"))
                ),
                "models": len(models),
                "prompts": len(prompts),
                "experiments": total_experiments,
                "cost": total_cost,
            },
            "active_run": active,
            "recent_runs": recent_runs[:5],
            "leaderboard": leaderboard[:5],
            "accuracy_trend": accuracy_trend[-20:],
        }