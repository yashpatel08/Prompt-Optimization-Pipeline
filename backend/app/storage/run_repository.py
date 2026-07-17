import json
from pathlib import Path
from dataclasses import asdict
from app.models.prompt import Prompt
from app.models.model import Model
from app.models.run import Run
from app.models.dataset import Dataset
from app.models.evaluation_result import EvaluationResult
from app.models.test_case import TestCase
from app.models.experiment import Experiment
from datetime import datetime
from app.models.evaluation_type import EvaluationType


class RunRepository:

    def save(
        self,
        run: Run,
    ):

        folder = Path("runs") / f"{run.created_at:%Y%m%d_%H%M%S}_{run.id[:8]}"

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            folder / "run.json",
            "w",
            encoding="utf8",
        ) as f:

            json.dump(
                asdict(run),
                f,
                indent=2,
                default=str,
            )

        return folder

    def load(
        self,
        folder: str,
    ) -> Run:

        folder = Path(folder)
        experiments_file = folder / "experiments.json"

        with open(experiments_file, encoding="utf-8") as f:
            data = json.load(f)

        experiments = []

        for e in data:

            prompt = Prompt(
                id=e["prompt"]["id"],
                name=e["prompt"]["name"],
                version=e["prompt"]["version"],
                system_prompt=e["prompt"].get("system_prompt", ""),
                author=e["prompt"].get("author", ""),
                description=e["prompt"].get("description", ""),
                tags=e["prompt"].get("tags", []),
                created_at=datetime.fromisoformat(e["prompt"]["created_at"]),
            )

            model = Model(
                id=e["model"]["id"],
                name=e["model"]["name"],
            )

            results = []

            for r in e["results"]:

                test_case = TestCase(
                    id=r["test_case"]["id"],
                    task=r["test_case"].get("task", ""),
                    input=r["test_case"]["input"],
                    reference=r["test_case"]["reference"],
                    evaluation=EvaluationType(
                        r["test_case"].get("evaluation", "exact_match")
                    ),
                    criteria=r["test_case"].get("criteria"),
                )

                results.append(
                    EvaluationResult(
                        test_case=test_case,
                        prompt_id=r["prompt_id"],
                        model=r["model"],
                        output=r["output"],
                        reasoning=r.get("reasoning"),
                        score=r["score"],
                        latency_ms=r["latency_ms"],
                        prompt_tokens=r["prompt_tokens"],
                        completion_tokens=r["completion_tokens"],
                        total_tokens=r["total_tokens"],
                    )
                )

            dataset = Dataset(
                name=e["dataset"]["name"],
                test_cases=[r.test_case for r in results],
            )

            experiments.append(
                Experiment(
                    id=e["id"],
                    model=model,
                    prompt=prompt,
                    dataset=dataset,
                    started_at=datetime.fromisoformat(e["started_at"]),
                    finished_at=datetime.fromisoformat(e["finished_at"]),
                    results=results,
                )
            )

        return Run(experiments)
