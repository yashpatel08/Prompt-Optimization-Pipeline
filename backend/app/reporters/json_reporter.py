import json
from pathlib import Path
from app.models.experiment import Experiment
from datetime import datetime


class JsonReporter:

    def save(
        self,
        experiments: list[Experiment],
        filename: str,
    ):
        data = []
        created_at = datetime.utcnow().isoformat()
        for experiment in experiments:
            data.append(
                {
                    "id": experiment.id,
                    "created_at": created_at,
                    "started_at": (
                        experiment.started_at.isoformat()
                        if experiment.started_at
                        else None
                    ),
                    "finished_at": (
                        experiment.finished_at.isoformat()
                        if experiment.finished_at
                        else None
                    ),
                    "duration_seconds": experiment.duration,
                    "model": {
                        "id": experiment.model.id,
                        "name": experiment.model.name,
                    },
                    "created_at": created_at,
                    "prompt": {
                        "id": experiment.prompt.id,
                        "name": experiment.prompt.name,
                        "version": experiment.prompt.version,
                        "system_prompt": experiment.prompt.system_prompt,
                        "author": experiment.prompt.author,
                        "description": experiment.prompt.description,
                        "tags": experiment.prompt.tags,
                        "created_at": experiment.prompt.created_at.isoformat(),
                    },
                    "dataset": {
                        "name": experiment.dataset.name,
                    },
                    "metrics": {
                        "accuracy": experiment.accuracy,
                        "passed": experiment.passed,
                        "failed": experiment.failed,
                        "avg_latency_ms": experiment.average_latency,
                        "min_latency_ms": experiment.min_latency,
                        "max_latency_ms": experiment.max_latency,
                        "avg_prompt_tokens": experiment.average_prompt_tokens,
                        "avg_completion_tokens": experiment.average_completion_tokens,
                        "avg_total_tokens": experiment.average_total_tokens,
                    },
                    "results": [
                        {
                            "test_case": {
                                "id": result.test_case.id,
                                "task": result.test_case.task,
                                "input": result.test_case.input,
                                "reference": result.test_case.reference,
                                "evaluation": result.test_case.evaluation.value,
                            },
                            "prompt_id": result.prompt_id,
                            "model": result.model,
                            "output": result.output,
                            "reasoning": result.reasoning,
                            "score": result.score,
                            "latency_ms": result.latency_ms,
                            "prompt_tokens": result.prompt_tokens,
                            "completion_tokens": result.completion_tokens,
                            "total_tokens": result.total_tokens,
                        }
                        for result in experiment.results
                    ],
                }
            )

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"Saved report to {filename}")
