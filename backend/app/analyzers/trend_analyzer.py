from collections import defaultdict

from app.models.run import Run
from app.models.trend import ExperimentTrend, TrendPoint


class TrendAnalyzer:

    def analyze(
        self,
        runs: list[Run],
        run_names: list[str],
    ) -> list[ExperimentTrend]:

        grouped = defaultdict(list)

        for run_name, run in zip(run_names, runs):

            for experiment in run.experiments:

                key = (
                    experiment.model.id,
                    experiment.prompt.id,
                )

                grouped[key].append(
                    (
                        experiment,
                        run_name,
                    )
                )

        trends = []

        for experiments in grouped.values():

            first = experiments[0][0]

            history = []

            for experiment, run_name in experiments:

                history.append(
                    TrendPoint(
                        run=run_name,
                        accuracy=experiment.accuracy,
                        latency=experiment.average_latency,
                        tokens=experiment.average_completion_tokens,
                    )
                )

            trends.append(
                ExperimentTrend(
                    model=first.model.name,
                    prompt=first.prompt.name,
                    history=history,
                )
            )

        return trends