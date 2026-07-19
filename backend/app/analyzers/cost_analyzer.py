from app.models.experiment import Experiment
from app.models.experiment_cost import ExperimentCost
from app.pricing.pricing_registery import PRICING


class CostAnalyzer:

    def analyze(
        self,
        experiment: Experiment,
    ) -> ExperimentCost:

        prompt_tokens = sum(
            r.prompt_tokens
            for r in experiment.results
        )

        completion_tokens = sum(
            r.completion_tokens
            for r in experiment.results
        )

        total_tokens = prompt_tokens + completion_tokens

        pricing = PRICING.get(
            experiment.model.id,
        )

        if pricing is None:

            input_cost = 0
            output_cost = 0

        else:

            input_cost = (
                prompt_tokens
                / 1_000_000
                * pricing.input_cost_per_million
            )

            output_cost = (
                completion_tokens
                / 1_000_000
                * pricing.output_cost_per_million
            )

        return ExperimentCost(
            model=experiment.model.name,
            prompt=experiment.prompt.name,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
            input_cost=input_cost,
            output_cost=output_cost,
            total_cost=input_cost + output_cost,
        )