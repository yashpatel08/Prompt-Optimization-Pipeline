from dataclasses import dataclass
from app.models.test_case import TestCase

@dataclass
class EvaluationResult:
    test_case: TestCase
    prompt_id: str
    model: str

    output: str
    score: float

    latency_ms: float

    prompt_tokens: int
    completion_tokens: int
    reasoning: str | None = None