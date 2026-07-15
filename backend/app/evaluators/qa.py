from app.evaluators.base import BaseEvaluator
from app.models.test_case import TestCase


class QAEvaluator(BaseEvaluator):

    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:

        reference = test_case.reference.strip().lower()
        candidate = output.strip().lower()

        return (
            1.0
            if (
                reference == candidate
                or reference in candidate
                or candidate in reference
            )
            else 0.0
        )
