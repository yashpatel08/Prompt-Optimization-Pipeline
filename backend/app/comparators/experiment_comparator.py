from app.models.comparison import Comparison
from app.models.experiment import Experiment
from app.models.test_case_comparison import TestCaseComparison


class ExperimentComparator:

    def compare(
        self,
        left: Experiment,
        right: Experiment,
    ) -> Comparison:

        if left.dataset.name != right.dataset.name:
            raise ValueError("Cannot compare different datasets.")
        test_case_comparisons = []

        for left_result, right_result in zip(
            left.results,
            right.results,
        ):
            test_case_comparisons.append(
                TestCaseComparison(
                    left=left_result,
                    right=right_result,
                )
            )
        return Comparison(
            left,
            right,
            test_cases=test_case_comparisons,
        )
