from dataclasses import dataclass, field

from app.models.leaderboard_entry import LeaderboardEntry


@dataclass
class Leaderboard:
    entries: list[LeaderboardEntry] = field(default_factory=list)