from dataclasses import dataclass
from app.models.regression import Regression

@dataclass
class RegressionResult:

    model: str
    prompt: str

    regressions: list[Regression]
    improvements: list[Regression]
    unchanged: list[Regression]