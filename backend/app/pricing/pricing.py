from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPricing:
    input_cost_per_million: float
    output_cost_per_million: float