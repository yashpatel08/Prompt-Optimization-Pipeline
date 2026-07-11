import time
from app.models.prompt import Prompt
from app.models.experiment import Experiment
from app.llm import ask
from app.normalizer import normalize
from app.evaluator import evaluate
from app.models.evaluation_result import EvaluationResult
from app.models.dataset import Dataset
from app.models.model import Model

class ExperimentRunner:

    def __init__(
        self,
        models: list[Model],
        prompts: list[Prompt],
        dataset: Dataset,
    ):
        self.prompts = prompts
        self.models = models
        self.dataset = dataset

    def run(self) -> list[Experiment]:
        # Create a list to store all experiments
        experiments = []
        for model in self.models:
            
            # Loop through each prompt
            for prompt in self.prompts:

                # Create a fresh list of results for this prompt
                results = []

                # Run every test case
                for test_case in self.dataset.test_cases:
                    # Ask the LLM
                    response = ask(
                        test_case.input,
                        prompt,
                        model.id,
                    )
                    # Normalize the output
                    clean_output = normalize(response.message.content)

                    # Evaluate the output
                    score = evaluate(
                        test_case,
                        clean_output,
                    )

                    # Create an EvaluationResult
                    result = EvaluationResult(
                        test_case=test_case,
                        prompt_id=prompt.id,
                        model=response.model,
                        output=clean_output,
                        score=score,
                        latency_ms=response.total_duration / 1_000_000,
                        prompt_tokens=response.prompt_eval_count,
                        completion_tokens=response.eval_count,
                    )

                    # Store the result
                    results.append(result)

                # Create an Experiment for this prompt
                experiment = Experiment(
                    model=model,
                    prompt=prompt,
                    dataset=self.dataset,
                    results=results,
                )

                # Store the experiment
                experiments.append(experiment)

        # Return all experiments
        return experiments
