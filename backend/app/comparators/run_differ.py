from app.models.run import Run
from app.models.run_diff import RunDiff
from app.models.experiment_diff import ExperimentDiff


class RunDiffer:

    def compare(
        self,
        previous: Run,
        latest: Run,
    ) -> RunDiff:

        diffs = []

        for latest_exp in latest.experiments:

            previous_exp = next(
                (
                    e
                    for e in previous.experiments
                    if e.model.id == latest_exp.model.id
                    and e.prompt.id == latest_exp.prompt.id
                    and e.dataset.name == latest_exp.dataset.name
                ),
                None,
            )

            if previous_exp is None:
                continue

            diffs.append(
                ExperimentDiff(
                    previous=previous_exp,
                    latest=latest_exp,

                    accuracy_diff=
                        latest_exp.accuracy
                        - previous_exp.accuracy,

                    latency_diff=
                        latest_exp.average_latency
                        - previous_exp.average_latency,

                    token_diff=
                        latest_exp.average_completion_tokens
                        - previous_exp.average_completion_tokens,

                    passed_diff=
                        latest_exp.passed
                        - previous_exp.passed,

                    failed_diff=
                        latest_exp.failed
                        - previous_exp.failed,
                )
            )

        return RunDiff(
            previous=previous,
            latest=latest,
            experiment_diffs=diffs,
        )