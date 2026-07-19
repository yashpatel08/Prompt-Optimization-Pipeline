from app.models.run_diff import RunDiff


class RunDiffReporter:

    def display(
        self,
        diff: RunDiff,
    ):

        print()
        print("=" * 80)
        print("Run Diff")
        print("=" * 80)

        for experiment in diff.experiment_diffs:

            print(
                f"{experiment.latest.model.name}"
                f" | "
                f"{experiment.latest.prompt.name}"
            )

            print("-" * 80)

            print(
                f"Accuracy : "
                f"{experiment.previous.accuracy:.2%}"
                f" -> "
                f"{experiment.latest.accuracy:.2%}"
                f" ({experiment.accuracy_diff:+.2%})"
            )

            print(
                f"Latency  : "
                f"{experiment.previous.average_latency/1000:.2f}s"
                f" -> "
                f"{experiment.latest.average_latency/1000:.2f}s"
                f" ({experiment.latency_diff/1000:+.2f}s)"
            )

            print(
                f"Tokens   : "
                f"{experiment.previous.average_completion_tokens:.1f}"
                f" -> "
                f"{experiment.latest.average_completion_tokens:.1f}"
                f" ({experiment.token_diff:+.1f})"
            )

            print(
                f"Passed   : "
                f"{experiment.previous.passed}"
                f" -> "
                f"{experiment.latest.passed}"
            )

            print(
                f"Failed   : "
                f"{experiment.previous.failed}"
                f" -> "
                f"{experiment.latest.failed}"
            )

            print("-" * 80)

        print("=" * 80)