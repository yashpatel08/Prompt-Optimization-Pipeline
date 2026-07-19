from dataclasses import dataclass

@dataclass
class Regression:

    test_case_id: str
    task: str

    previous_score: float
    latest_score: float
    expected: str
    previous_output: str
    latest_output: str
    status: str