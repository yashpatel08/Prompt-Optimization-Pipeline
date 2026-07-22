from pathlib import Path
import json


class DatasetService:

    def list(self):

        root = Path("datasets")

        datasets = []

        for file in sorted(root.glob("*.json")):

            with open(file, encoding="utf-8") as f:
                data = json.load(f)

            datasets.append(
                {
                    "id": file.stem,
                    "name": file.stem.replace("_", " ").title(),
                    "filename": file.name,
                    "test_cases": len(data),
                    "size": file.stat().st_size,
                    "updated_at": file.stat().st_mtime,
                }
            )

        return datasets