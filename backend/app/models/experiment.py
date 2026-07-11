from dataclasses import dataclass
from app.models.evaluation_result import EvaluationResult
from app.models.prompt import Prompt
from app.models.model import Model
from app.models.dataset import Dataset
from statistics import mean

@dataclass
class Experiment:
    model: Model
    prompt: Prompt
    dataset: Dataset
    results: list[EvaluationResult]

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def passed(self) -> int:
        return sum(result.score == 1.0 for result in self.results)

    @property
    def failed(self) -> int:
        return self.total - self.passed

    @property
    def accuracy(self) -> float:
        if self.total == 0:
            return 0.0

        return self.passed / self.total

    @property
    def average_latency(self) -> float:
        if self.total == 0:
            return 0.0

        return mean(result.latency_ms for result in self.results)

    @property
    def average_prompt_tokens(self) -> float:
        if self.total == 0:
            return 0.0

        return (
            sum(result.prompt_tokens for result in self.results)
            / self.total
        )

    @property
    def average_completion_tokens(self) -> float:
        if self.total == 0:
            return 0.0

        return (
            sum(result.completion_tokens for result in self.results)
            / self.total
        )

    @property
    def average_total_tokens(self) -> float:
        if self.total == 0:
            return 0.0

        return (
            sum(
                result.prompt_tokens + result.completion_tokens
                for result in self.results
            )
            / self.total
        )
    
    @property
    def min_latency(self) -> float:
        if self.total == 0:
            return 0.0

        return min(result.latency_ms for result in self.results)

    @property
    def max_latency(self) -> float:
        if self.total == 0:
            return 0.0

        return max(result.latency_ms for result in self.results)