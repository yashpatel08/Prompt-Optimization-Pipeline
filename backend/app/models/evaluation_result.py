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
    total_tokens: int
    reasoning: str | None = None
    input_cost: float = 0.0
    output_cost: float = 0.0
    total_cost: float = 0.0