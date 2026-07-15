from dataclasses import dataclass, field

from app.models.experiment import Experiment
from app.models.test_case_comparison import TestCaseComparison


@dataclass
class Comparison:
    left: Experiment
    right: Experiment

    test_cases: list[TestCaseComparison] = field(default_factory=list)

    @property
    def accuracy_diff(self):
        return self.right.accuracy - self.left.accuracy

    @property
    def passed_diff(self):
        return self.right.passed - self.left.passed

    @property
    def latency_diff(self):
        return self.right.average_latency - self.left.average_latency

    @property
    def token_diff(self):
        return (
            self.right.average_completion_tokens
            - self.left.average_completion_tokens
        )