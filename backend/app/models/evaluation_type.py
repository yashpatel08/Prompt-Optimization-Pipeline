from enum import Enum


class EvaluationType(Enum):
    EXACT_MATCH = "exact_match"
    CONTAINS = "contains"
    QA="qa"
    LLM_JUDGE = "llm_judge"