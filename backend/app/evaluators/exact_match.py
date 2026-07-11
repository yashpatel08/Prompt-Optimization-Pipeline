from app.evaluators.base import BaseEvaluator
from app.models.test_case import TestCase


class ExactMatchEvaluator(BaseEvaluator):

    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:

        return 1.0 if test_case.reference == output else 0.0