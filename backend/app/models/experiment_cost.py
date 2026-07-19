from dataclasses import dataclass


@dataclass
class ExperimentCost:

    model: str
    prompt: str

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    input_cost: float
    output_cost: float
    total_cost: float