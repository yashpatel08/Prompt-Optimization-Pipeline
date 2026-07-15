from ollama import chat

from app.evaluators.base import BaseEvaluator
from app.models.test_case import TestCase


class LLMJudgeEvaluator(BaseEvaluator):

    def evaluate(
        self,
        test_case: TestCase,
        output: str,
    ) -> float:

        response = chat(
            model="hermes3",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an evaluation system.

Compare the reference answer and the candidate answer.

Score 1 if:
- They convey the same meaning.
- Minor wording differences are acceptable.
- Shorter summaries are acceptable if they preserve the important facts.

Score 0 if:
- Important information is missing.
- Facts are incorrect.
- The answer does not satisfy the task.

Return ONLY:
1
or
0
""",
                },
                {
                    "role": "user",
                    "content": f"""
Reference:
{test_case.reference}

Candidate:
{output}
""",
                },
            ],
            think=False,
        )

        answer = response.message.content.strip()

        return 1.0 if answer.startswith("1") else 0.0