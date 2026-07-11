from dataclasses import dataclass

from app.models.test_case import TestCase


@dataclass
class Dataset:
    name: str
    test_cases: list[TestCase]