from dataclasses import dataclass, field

from app.models.failure import Failure


@dataclass
class FailureReport:
    failures: list[Failure] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.failures)