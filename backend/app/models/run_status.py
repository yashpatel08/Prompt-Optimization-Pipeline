from dataclasses import dataclass


@dataclass
class RunStatus:
    run_id: str
    status: str

    progress: int

    current_model: str | None = None
    current_prompt: str | None = None
    current_test_case: str | None = None

    started_at: str | None = None
    finished_at: str | None = None