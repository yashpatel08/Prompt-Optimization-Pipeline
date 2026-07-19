from dataclasses import dataclass

from app.models.run import Run
from app.models.experiment_diff import ExperimentDiff


@dataclass
class RunDiff:

    previous: Run
    latest: Run

    experiment_diffs: list[ExperimentDiff]