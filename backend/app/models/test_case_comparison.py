from dataclasses import dataclass

from app.models.evaluation_result import EvaluationResult


@dataclass
class TestCaseComparison:
    left: EvaluationResult
    right: EvaluationResult

    @property
    def same_score(self) -> bool:
        return self.left.score == self.right.score

    @property
    def score_diff(self) -> float:
        return self.right.score - self.left.score

    @property
    def latency_diff(self) -> float:
        return self.right.latency_ms - self.left.latency_ms

    @property
    def token_diff(self) -> int:
        return (
            self.right.prompt_tokens
            + self.right.completion_tokens
            - self.left.prompt_tokens
            - self.left.completion_tokens
        )

    @property
    def winner(self):

        if self.left.score != self.right.score:
            return "Left" if self.left.score > self.right.score else "Right"

        if self.left.completion_tokens != self.right.completion_tokens:
            return (
                "Left"
                if self.left.completion_tokens < self.right.completion_tokens
                else "Right"
            )

        if self.left.latency_ms != self.right.latency_ms:
            return (
                "Left"
                if self.left.latency_ms < self.right.latency_ms
                else "Right"
            )

        return "Tie"