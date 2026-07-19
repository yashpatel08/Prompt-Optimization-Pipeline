from app.models.experiment_cost import ExperimentCost


class CostReporter:

    def display(
        self,
        reports: list[ExperimentCost],
    ):

        print()
        print("=" * 90)
        print("Cost Report")
        print("=" * 90)

        total = 0

        for report in reports:

            total += report.total_cost

            print()
            print(
                f"{report.model} | {report.prompt}"
            )
            print("-" * 90)

            print(
                f"Prompt Tokens     : {report.prompt_tokens:,}"
            )

            print(
                f"Completion Tokens : {report.completion_tokens:,}"
            )

            print(
                f"Total Tokens      : {report.total_tokens:,}"
            )

            print(
                f"Input Cost        : ${report.input_cost:.6f}"
            )

            print(
                f"Output Cost       : ${report.output_cost:.6f}"
            )

            print(
                f"Total Cost        : ${report.total_cost:.6f}"
            )

        print()
        print("=" * 90)
        print(f"Run Total Cost : ${total:.6f}")
        print("=" * 90)