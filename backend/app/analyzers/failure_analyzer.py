from app.models.experiment import Experiment
from app.models.failure import Failure
from app.models.failure_report import FailureReport


class FailureAnalyzer:

    def analyze(
        self,
        experiment: Experiment,
    ) -> FailureReport:

        failures = []

        for result in experiment.results:

            if result.score == 0:
                failures.append(Failure(result))

        return FailureReport(failures)