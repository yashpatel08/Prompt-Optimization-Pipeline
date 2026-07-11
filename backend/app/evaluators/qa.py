from app.evaluators.base import BaseEvaluator
from app.models.test_case import TestCase

class QAEvaluator(BaseEvaluator):

    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:

        reference = test_case.reference.strip().lower()
        output = output.strip().lower()

        if reference == output:
            return 1.0

        if reference in output:
            return 1.0

        if output in reference:
            return 1.0

        return 0.0