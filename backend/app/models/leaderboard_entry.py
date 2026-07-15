from dataclasses import dataclass

from app.models.experiment import Experiment


@dataclass
class LeaderboardEntry:
    rank: int
    experiment: Experiment  