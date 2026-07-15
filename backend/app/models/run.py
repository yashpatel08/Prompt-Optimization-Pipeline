from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from app.models.experiment import Experiment


@dataclass
class Run:
    experiments: list[Experiment]

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)