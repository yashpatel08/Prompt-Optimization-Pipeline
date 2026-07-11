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
