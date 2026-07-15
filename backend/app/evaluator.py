from app.models.test_case import TestCase
from app.models.evaluation_type import EvaluationType

from app.evaluators.exact_match import ExactMatchEvaluator
from app.evaluators.contains import ContainsEvaluator
from app.evaluators.qa import QAEvaluator
from app.evaluators.llm_judge import LLMJudgeEvaluator

EVALUATORS = {
    EvaluationType.EXACT_MATCH: ExactMatchEvaluator(),
    EvaluationType.CONTAINS: ContainsEvaluator(),
    EvaluationType.QA: QAEvaluator(),
    EvaluationType.LLM_JUDGE: LLMJudgeEvaluator(),
}


def evaluate(
    test_case: TestCase,
    output: str,
) -> float:

    evaluator = EVALUATORS.get(test_case.evaluation)

    if evaluator is None:
        raise ValueError(f"Unknown evaluation type: {test_case.evaluation}")

    return evaluator.evaluate(
        test_case,
        output,
    )
