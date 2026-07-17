from pathlib import Path
import json
from datetime import datetime

from app.models.run_summary import RunSummary


class RunHistory:

    REPORTS_DIR = Path("reports")

    def load(self) -> list[RunSummary]:

        runs = []

        if not self.REPORTS_DIR.exists():
            return runs

        for folder in self.REPORTS_DIR.iterdir():

            if not folder.is_dir():
                continue

            experiments = folder / "experiments.json"

            if not experiments.exists():
                continue

            with open(experiments, encoding="utf-8") as f:
                data = json.load(f)

            runs.append(
                RunSummary(
                    id=folder.name,
                    created_at=datetime.fromtimestamp(folder.stat().st_ctime),
                    experiments=len(data),
                    path=str(folder),
                )
            )

        runs.sort(
            key=lambda r: r.created_at,
            reverse=True,
        )

        return runs