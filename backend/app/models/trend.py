from dataclasses import dataclass


@dataclass
class TrendPoint:

    run: str
    accuracy: float
    latency: float
    tokens: float


@dataclass
class ExperimentTrend:

    model: str
    prompt: str
    history: list[TrendPoint]