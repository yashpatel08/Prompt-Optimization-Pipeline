import json
from pathlib import Path
from app.models.comparison import Comparison

class ComparisonReporter:

    def display(self, comparison: Comparison):

        def format_latency(ms: float) -> str:
            if ms >= 1000:
                return f"{ms / 1000:.2f} s"
            return f"{ms:.1f} ms"

        def format_diff(value: float, suffix: str = "") -> str:
            if value > 0:
                return f"+{value:.2f}{suffix}"
            return f"{value:.2f}{suffix}"

        left = comparison.left
        right = comparison.right

        print()
        print("=" * 75)
        print("Experiment Comparison")
        print("=" * 75)

        print(f"Dataset : {left.dataset.name}")
        print(
            f"Left    : {left.model.name} | {left.prompt.name} (v{left.prompt.version})"
        )
        print(
            f"Right   : {right.model.name} | {right.prompt.name} (v{right.prompt.version})"
        )

        print("-" * 75)

        print(f"{'Metric':<22}" f"{'Left':>15}" f"{'Right':>15}" f"{'Δ':>15}")

        print("-" * 75)

        print(
            f"{'Accuracy':<22}"
            f"{left.accuracy:>15.2%}"
            f"{right.accuracy:>15.2%}"
            f"{format_diff(comparison.accuracy_diff * 100, '%'):>15}"
        )

        print(
            f"{'Passed':<22}"
            f"{left.passed:>15}"
            f"{right.passed:>15}"
            f"{comparison.passed_diff:>15}"
        )

        print(
            f"{'Avg Latency':<22}"
            f"{format_latency(left.average_latency):>15}"
            f"{format_latency(right.average_latency):>15}"
            f"{format_diff(comparison.latency_diff / 1000, ' s'):>15}"
        )

        print(
            f"{'Avg Tokens':<22}"
            f"{left.average_completion_tokens:>15.1f}"
            f"{right.average_completion_tokens:>15.1f}"
            f"{format_diff(comparison.token_diff):>15}"
        )

        print("=" * 75)

        print()


        print("Per Test Case Comparison")
        print("-" * 75)

        for test_case in comparison.test_cases:

            left = test_case.left
            right = test_case.right

            print(f"{left.test_case.id}")
            print(f"Expected : {left.test_case.reference}")
            print(f"Left     : {left.output}")
            print(f"Right    : {right.output}")
            print(f"Scores   : {left.score} -> {right.score}")
            print(
                f"Latency  : "
                f"{left.latency_ms:.0f} ms -> "
                f"{right.latency_ms:.0f} ms"
            )
            print(f"Winner   : {test_case.winner}")
            print("-" * 75)

        print("-" * 75)
    
    def save(
        self,
        comparisons: list[Comparison],
        filename: str,
    ):
        data = []

        for comparison in comparisons:
            data.append(
                {
                    "left": {
                        "experiment_id": comparison.left.id,
                        "model": comparison.left.model.name,
                        "prompt": comparison.left.prompt.name,
                    },
                    "right": {
                        "experiment_id": comparison.right.id,
                        "model": comparison.right.model.name,
                        "prompt": comparison.right.prompt.name,
                    },
                    "summary": {
                        "accuracy_diff": comparison.accuracy_diff,
                        "passed_diff": comparison.passed_diff,
                        "latency_diff_ms": comparison.latency_diff,
                        "token_diff": comparison.token_diff,
                    },
                    "test_cases": [
                        {
                            "id": tc.left.test_case.id,
                            "left_output": tc.left.output,
                            "right_output": tc.right.output,
                            "left_score": tc.left.score,
                            "right_score": tc.right.score,
                            "winner": tc.winner,
                            "left_latency_ms": tc.left.latency_ms,
                            "right_latency_ms": tc.right.latency_ms,
                        }
                        for tc in comparison.test_cases
                    ],
                }
            )

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"Saved comparisons to {filename}")
