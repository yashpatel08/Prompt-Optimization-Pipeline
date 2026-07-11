from app.models.comparison import Comparison
from app.models.experiment import Experiment


class ExperimentComparator:

    def compare(
        self,
        left: Experiment,
        right: Experiment,
    ) -> Comparison:

        if left.dataset.name != right.dataset.name:
            raise ValueError(
                "Cannot compare different datasets."
            )

        return Comparison(left, right)