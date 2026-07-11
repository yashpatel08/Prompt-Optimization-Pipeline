from dataclasses import dataclass
from app.models.experiment import Experiment


@dataclass
class Comparison:
    left: Experiment
    right: Experiment

    @property
    def accuracy_diff(self):
        return self.right.accuracy - self.left.accuracy

    @property
    def latency_diff(self):
        return (
            self.right.average_latency
            - self.left.average_latency
        )

    @property
    def token_diff(self):
        return (
            self.right.average_completion_tokens
            - self.left.average_completion_tokens
        )

    @property
    def passed_diff(self):
        return self.right.passed - self.left.passed