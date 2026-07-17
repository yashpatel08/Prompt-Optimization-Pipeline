from app.models.run import Run
from app.models.run_comparison import RunComparison


class RunComparator:

    def compare(
        self,
        left: Run,
        right: Run,
    ) -> RunComparison:

        left_accuracy = sum(e.accuracy for e in left.experiments) / len(left.experiments)
        right_accuracy = sum(e.accuracy for e in right.experiments) / len(right.experiments)

        left_latency = sum(e.average_latency for e in left.experiments) / len(left.experiments)
        right_latency = sum(e.average_latency for e in right.experiments) / len(right.experiments)

        left_tokens = sum(
            e.average_completion_tokens
            for e in left.experiments
        ) / len(left.experiments)

        right_tokens = sum(
            e.average_completion_tokens
            for e in right.experiments
        ) / len(right.experiments)

        return RunComparison(
            left=left,
            right=right,
            accuracy_diff=right_accuracy-left_accuracy,
            latency_diff=right_latency-left_latency,
            token_diff=right_tokens-left_tokens,
            experiment_diff=len(right.experiments)-len(left.experiments),
        )