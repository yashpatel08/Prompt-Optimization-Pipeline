from dataclasses import dataclass, field
from app.models.evaluation_result import EvaluationResult
from app.models.prompt import Prompt
from app.models.model import Model
from app.models.dataset import Dataset
from statistics import mean
from datetime import datetime
from uuid import uuid4
from app.models.experiment_cost import ExperimentCost

@dataclass
class Experiment:
    model: Model
    prompt: Prompt
    dataset: Dataset
    results: list[EvaluationResult]

    id: str = field(default_factory=lambda: str(uuid4()))
    started_at: datetime | None = None
    finished_at: datetime | None = None

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

        return sum(result.prompt_tokens for result in self.results) / self.total

    @property
    def average_completion_tokens(self) -> float:
        if self.total == 0:
            return 0.0

        return sum(result.completion_tokens for result in self.results) / self.total

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

    @property
    def duration(self) -> float:
        if self.started_at and self.finished_at:
            return (
                self.finished_at - self.started_at
            ).total_seconds()

        return 0.0
    
    @property
    def cost(self) -> ExperimentCost:

        return ExperimentCost(
            model=self.model.name,
            prompt=self.prompt.name,

            prompt_tokens=sum(
                result.prompt_tokens
                for result in self.results
            ),

            completion_tokens=sum(
                result.completion_tokens
                for result in self.results
            ),

            total_tokens=sum(
                result.total_tokens
                for result in self.results
            ),

            input_cost=sum(
                result.input_cost
                for result in self.results
            ),

            output_cost=sum(
                result.output_cost
                for result in self.results
            ),

            total_cost=sum(
                result.total_cost
                for result in self.results
            ),
        )