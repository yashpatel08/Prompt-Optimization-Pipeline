from pathlib import Path
from datetime import datetime


class RunManager:

    def __init__(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.run_dir = Path("reports") / f"run_{timestamp}"
        self.run_dir.mkdir(parents=True, exist_ok=True)

    def path(self, filename: str) -> str:
        return str(self.run_dir / filename)