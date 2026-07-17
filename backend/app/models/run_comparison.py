from dataclasses import dataclass

from app.models.run import Run


@dataclass
class RunComparison:
    left: Run
    right: Run

    accuracy_diff: float
    latency_diff: float
    token_diff: float
    experiment_diff: int