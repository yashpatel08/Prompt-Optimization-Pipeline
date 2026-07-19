from dataclasses import dataclass

from app.models.experiment import Experiment


@dataclass
class ExperimentDiff:

    previous: Experiment
    latest: Experiment

    accuracy_diff: float
    latency_diff: float
    token_diff: float

    passed_diff: int
    failed_diff: int