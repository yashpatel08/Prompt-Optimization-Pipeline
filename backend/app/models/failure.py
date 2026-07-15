from dataclasses import dataclass

from app.models.evaluation_result import EvaluationResult


@dataclass
class Failure:
    result: EvaluationResult

    @property
    def expected(self) -> str:
        return self.result.test_case.reference

    @property
    def actual(self) -> str:
        return self.result.output