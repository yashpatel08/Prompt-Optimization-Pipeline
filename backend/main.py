from app.llm import ask
from app.prompts import prompts
from app.experiment_runner import ExperimentRunner
from app.reporters.console_reporter import ConsoleReporter
from app.datasets.loader import DatasetLoader
from app.model_registry import models
from app.reporters.json_reporter import JsonReporter
from app.reporters.comparison_reporter import ComparisonReporter
from app.comparators.experiment_comparator import ExperimentComparator

loader = DatasetLoader()

dataset = loader.load("datasets/qa.json")

runner = ExperimentRunner(prompts=prompts, dataset=dataset, models=models)


def main():
    runner = ExperimentRunner(prompts=prompts, dataset=dataset, models=models)
    experiments = runner.run()

    ConsoleReporter().display(experiments, verbose=False)
    JsonReporter().save(experiments, "reports/results.json")
    comparator = ExperimentComparator()

    for i in range(0, len(experiments), 2):
        comparison = comparator.compare(
            experiments[i],
            experiments[i + 1],
        )

        ComparisonReporter().display(comparison)


if __name__ == "__main__":
    main()
