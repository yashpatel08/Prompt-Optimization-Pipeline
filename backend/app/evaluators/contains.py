from app.evaluators.base import BaseEvaluator
from app.models.test_case import TestCase


class ContainsEvaluator(BaseEvaluator):

    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:

        reference = test_case.reference.lower()

        candidate = output.lower()

        return 1.0 if reference in candidate else 0.0
