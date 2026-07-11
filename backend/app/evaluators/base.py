from abc import ABC, abstractmethod

from app.models.test_case import TestCase


class BaseEvaluator(ABC):

    @abstractmethod
    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:
        pass