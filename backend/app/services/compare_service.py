from statistics import mean

from app.history.run_history import RunHistory
from app.storage.run_repository import RunRepository


class CompareService:

    def options(self):

        history = RunHistory().load()

        repo = RunRepository()

        items = []

        for summary in history:

            run = repo.load(summary.path)

            if run is None:
                continue

            models = sorted(
                {
                    exp.model.name
                    for exp in run.experiments
                }
            )

            prompts = sorted(
                {
                    exp.prompt.name
                    for exp in run.experiments
                }
            )

            items.append(
                {
                    "id": summary.id,
                    "name": summary.id[:8],
                    "created_at": summary.created_at.isoformat(),
                    "models": models,
                    "prompts": prompts,
                    "experiments": len(run.experiments),
                }
            )

        items.sort(
            key=lambda x: x["created_at"],
            reverse=True,
        )

        return items

    def compare(
        self,
        left: str,
        right: str,
    ):

        history = RunHistory().load()

        summaries = {
            item.id: item
            for item in history
        }

        left_summary = summaries.get(left)
        right_summary = summaries.get(right)

        if left_summary is None:
            return {
                "error": "Left run not found"
            }

        if right_summary is None:
            return {
                "error": "Right run not found"
            }

        repo = RunRepository()

        left_run = repo.load(left_summary.path)
        right_run = repo.load(right_summary.path)

        if left_run is None:
            return {
                "error": "Left run data not found"
            }

        if right_run is None:
            return {
                "error": "Right run data not found"
            }

        left_metrics = self._summary(left_run)
        right_metrics = self._summary(right_run)

        if left_metrics["accuracy"] >= right_metrics["accuracy"]:
            winner = {
                "name": left_summary.id,
                "improvement": left_metrics["accuracy"] - right_metrics["accuracy"],
            }
        else:
            winner = {
                "name": right_summary.id,
                "improvement": right_metrics["accuracy"] - left_metrics["accuracy"],
            }

        return {
            "summary": winner,
            "a": {
                "model": left_run.experiments[0].model.name,
                **left_metrics,
            },
            "b": {
                "model": right_run.experiments[0].model.name,
                **right_metrics,
            },
        }

    def _summary(self, run):

        experiments = run.experiments

        return {
            "accuracy": mean(
                exp.accuracy
                for exp in experiments
            ),
            "latency_ms": mean(
                exp.average_latency
                for exp in experiments
            ),
            "prompt_tokens": sum(
                exp.cost.prompt_tokens
                for exp in experiments
            ),
            "completion_tokens": sum(
                exp.cost.completion_tokens
                for exp in experiments
            ),
            "cost": sum(
                exp.cost.total_cost
                for exp in experiments
            ),
            "failures": sum(
                exp.failed
                for exp in experiments
            ),
        }