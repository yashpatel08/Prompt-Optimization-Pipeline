from app.models.run_comparison import RunComparison


class RunComparisonReporter:

    def display(
        self,
        comparison: RunComparison,
    ):

        print()
        print("=" * 75)
        print("Run Comparison")
        print("=" * 75)

        print(f"Left  : {comparison.left.id}")
        print(f"Right : {comparison.right.id}")

        print("-" * 75)

        print(
            f"{'Metric':<20}"
            f"{'Difference':>20}"
        )

        print("-" * 75)

        print(
            f"{'Accuracy':<20}"
            f"{comparison.accuracy_diff*100:>18.2f}%"
        )

        print(
            f"{'Latency':<20}"
            f"{comparison.latency_diff/1000:>18.2f}s"
        )

        print(
            f"{'Tokens':<20}"
            f"{comparison.token_diff:>18.2f}"
        )

        print(
            f"{'Experiments':<20}"
            f"{comparison.experiment_diff:>18}"
        )

        print("=" * 75)
        print()