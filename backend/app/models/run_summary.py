from dataclasses import dataclass
from datetime import datetime

@dataclass
class RunSummary:
    id: str
    created_at: datetime
    experiments: int
    path: str