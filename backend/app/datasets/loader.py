import json
from pathlib import Path

from app.models.dataset import Dataset
from app.models.test_case import TestCase
from app.models.evaluation_type import EvaluationType

class DatasetLoader:

    def load(self, path: str) -> Dataset:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        test_cases = []

        for item in data:
            test_case = TestCase(
                id=item["id"],
                task=item["task"],
                input=item["input"],
                reference=item["reference"],
                evaluation=EvaluationType(item["evaluation"]),
            )

            test_cases.append(test_case)
        
        return Dataset(
            name=Path(path).stem,
            test_cases=test_cases,
        )