from dataclasses import dataclass
from app.models.evaluation_type import EvaluationType

@dataclass
class TestCase:
    id: str
    task: str
    input: str
    reference: str
    evaluation: EvaluationType

    criteria: str | None = None