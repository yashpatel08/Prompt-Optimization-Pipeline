from app.models.run_summary import RunSummary


class HistoryReporter:

    def display(
        self,
        runs: list[RunSummary],
    ):

        print()
        print("=" * 70)
        print("Run History")
        print("=" * 70)

        print(
            f"{'Run':<28}"
            f"{'Created':<22}"
            f"{'Experiments':>12}"
        )

        print("-" * 70)

        for run in runs:

            print(
                f"{run.id:<28}"
                f"{run.created_at.strftime('%Y-%m-%d %H:%M'):<22}"
                f"{run.experiments:>12}"
            )

        print("=" * 70)
        print()