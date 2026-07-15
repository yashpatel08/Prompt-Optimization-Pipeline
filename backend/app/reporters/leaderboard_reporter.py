import json
from pathlib import Path
from app.models.leaderboard import Leaderboard

class LeaderboardReporter:

    def display(
        self,
        leaderboard: Leaderboard,
    ):

        print()
        print("=" * 78)
        print("Leaderboard")
        print("=" * 78)

        print(
            f"{'Rank':<6}"
            f"{'Model':<18}"
            f"{'Prompt':<18}"
            f"{'Accuracy':>12}"
            f"{'Latency':>12}"
            f"{'Tokens':>12}"
        )

        print("-" * 78)

        for entry in leaderboard.entries:

            experiment = entry.experiment

            print(
                f"{entry.rank:<6}"
                f"{experiment.model.name:<18}"
                f"{experiment.prompt.name:<18}"
                f"{experiment.accuracy:>11.2%}"
                f"{experiment.average_latency/1000:>10.2f}s"
                f"{experiment.average_completion_tokens:>12.1f}"
            )

        print("=" * 78)
        print()
    
    def save(
        self,
        leaderboard: Leaderboard,
        filename: str,
    ):
        data = []

        for entry in leaderboard.entries:
            experiment = entry.experiment

            data.append(
                {
                    "rank": entry.rank,
                    "experiment_id": experiment.id,
                    "model": experiment.model.name,
                    "prompt": {
                        "id": experiment.prompt.id,
                        "name": experiment.prompt.name,
                        "version": experiment.prompt.version,
                    },
                    "dataset": experiment.dataset.name,
                    "metrics": {
                        "accuracy": experiment.accuracy,
                        "passed": experiment.passed,
                        "failed": experiment.failed,
                        "average_latency_ms": experiment.average_latency,
                        "average_prompt_tokens": experiment.average_prompt_tokens,
                        "average_completion_tokens": experiment.average_completion_tokens,
                        "average_total_tokens": experiment.average_total_tokens,
                    },
                }
            )

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"Saved leaderboard to {filename}")