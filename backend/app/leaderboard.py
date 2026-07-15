from app.models.experiment import Experiment
from app.models.leaderboard import Leaderboard
from app.models.leaderboard_entry import LeaderboardEntry


class LeaderboardBuilder:

    def build(
        self,
        experiments: list[Experiment],
    ) -> Leaderboard:

        ranked = sorted(
            experiments,
            key=lambda experiment: (
                -experiment.accuracy,
                experiment.average_latency,
                experiment.average_completion_tokens,
            ),
        )

        entries = []

        for rank, experiment in enumerate(ranked, start=1):
            entries.append(
                LeaderboardEntry(
                    rank=rank,
                    experiment=experiment,
                )
            )

        return Leaderboard(entries)