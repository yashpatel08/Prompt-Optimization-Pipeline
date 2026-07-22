from app.models.run_status import RunStatus


class RunStatusService:

    _runs: dict[str, RunStatus] = {}

    def create(self, run_id: str):

        self._runs[run_id] = RunStatus(
            run_id=run_id,
            status="running",
            progress=0,
        )

    def get(self, run_id: str):

        return self._runs.get(run_id)

    def update(
        self,
        run_id: str,
        **kwargs,
    ):

        status = self._runs.get(run_id)

        if status is None:
            return

        for key, value in kwargs.items():
            setattr(status, key, value)

    def all(self):

        return list(self._runs.values())