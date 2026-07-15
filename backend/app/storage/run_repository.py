import json
from pathlib import Path
from dataclasses import asdict

from app.models.run import Run


class RunRepository:

    def save(
        self,
        run: Run,
    ):

        folder = (
            Path("runs")
            / f"{run.created_at:%Y%m%d_%H%M%S}_{run.id[:8]}"
        )

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