import json
from pathlib import Path

from app.models.failure_report import FailureReport
from app.models.experiment import Experiment


class FailureReporter:

    def display(
        self,
        experiment: Experiment,
        report: FailureReport,
    ):
        print()
        print("=" * 70)
        print("Failure Analysis")
        print("=" * 70)
        print(f"Model  : {experiment.model.name}")
        print(f"Prompt : {experiment.prompt.name}")
        print("-" * 70)

        if report.total == 0:
            print("No failed test cases.")
            return

        for failure in report.failures:
            result = failure.result

            print(result.test_case.id)
            print(f"Question : {result.test_case.input}")
            print(f"Expected : {failure.expected}")
            print(f"Actual   : {failure.actual}")
            print(f"Score    : {result.score}")
            print("-" * 70)

        print()

    def save(
        self,
        reports: list[FailureReport],
        filename: str,
    ):
        data = []

        for experiment, report in reports:
            data.append(
                {
                    "experiment_id": experiment.id,
                    "model": experiment.model.name,
                    "prompt": experiment.prompt.name,
                    "total_failures": report.total,
                    "failures": [
                        {
                            "test_case_id": failure.result.test_case.id,
                            "question": failure.result.test_case.input,
                            "expected": failure.expected,
                            "actual": failure.actual,
                            "score": failure.result.score,
                        }
                        for failure in report.failures
                    ],
                }
            )

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"Saved failure report to {filename}")