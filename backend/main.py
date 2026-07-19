from app.llm import ask
from app.prompts import prompts
from app.experiment_runner import ExperimentRunner
from app.reporters.console_reporter import ConsoleReporter
from app.datasets.loader import DatasetLoader
from app.model_registry import models
from app.reporters.json_reporter import JsonReporter
from app.reporters.comparison_reporter import ComparisonReporter
from app.comparators.experiment_comparator import ExperimentComparator
from app.leaderboard import LeaderboardBuilder
from app.reporters.leaderboard_reporter import LeaderboardReporter
from app.analyzers.failure_analyzer import FailureAnalyzer
from app.reporters.failure_reporter import FailureReporter
from app.models.run import Run
from app.storage.run_repository import RunRepository
from app.run_manager import RunManager
from app.history.run_history import RunHistory
from app.reporters.history_reporter import HistoryReporter
from app.comparators.run_comparator import RunComparator
from app.reporters.run_comparison_reporter import RunComparisonReporter
from app.comparators.run_differ import RunDiffer
from app.reporters.run_diff_reporter import RunDiffReporter
from app.history.trend_history import TrendHistory
from app.analyzers.trend_analyzer import TrendAnalyzer
from app.reporters.trend_reporter import TrendReporter
from app.analyzers.regression_detector import RegressionDetector
from app.reporters.regression_reporter import RegressionReporter
from app.analyzers.cost_analyzer import CostAnalyzer
from app.reporters.cost_reporter import CostReporter

loader = DatasetLoader()

dataset = loader.load("datasets/qa.json")

runner = ExperimentRunner(prompts=prompts, dataset=dataset, models=models)


def main():
    experiments = runner.run()

    run_manager = RunManager()

    ConsoleReporter().display(experiments, verbose=False)

    JsonReporter().save(
        experiments,
        run_manager.path("experiments.json"),
    )

    run = Run(experiments)
    RunRepository().save(run)

    leaderboard = LeaderboardBuilder().build(experiments)

    LeaderboardReporter().save(
        leaderboard,
        run_manager.path("leaderboard.json"),
    )

    comparator = ExperimentComparator()

    comparisons = []

    for i in range(0, len(experiments), 2):
        comparisons.append(
            comparator.compare(
                experiments[i],
                experiments[i + 1],
            )
        )

    ComparisonReporter().save(
        comparisons,
        run_manager.path("comparisons.json"),
    )

    failure_reports = []

    for experiment in experiments:
        report = FailureAnalyzer().analyze(experiment)

        failure_reports.append((experiment, report))

    FailureReporter().save(
        failure_reports,
        run_manager.path("failures.json"),
    )

    history = RunHistory().load()
    HistoryReporter().display(history)

    if len(history) >= 2:

        previous = RunRepository().load(history[1].path)
        latest = RunRepository().load(history[0].path)

        comparison = RunComparator().compare(
            previous,
            latest,
        )

        RunComparisonReporter().display(comparison)

    diff = RunDiffer().compare(
        previous,
        latest,
    )

    RunDiffReporter().display(diff)

    runs, names = TrendHistory().load()

    trends = TrendAnalyzer().analyze(
        runs,
        names,
    )

    TrendReporter().display(trends)

    regressions = RegressionDetector().detect(
        previous,
        latest,
    )

    RegressionReporter().display(regressions)

    costs = []

    analyzer = CostAnalyzer()

    for experiment in experiments:
        costs.append(analyzer.analyze(experiment))

    CostReporter().display(costs)

if __name__ == "__main__":
    main()
