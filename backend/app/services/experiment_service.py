from app.history.run_history import RunHistory
from app.services.run_status_service import RunStatusService


class ExperimentService:

    def list(self):

        history = RunHistory().load()

        statuses = {
            s.run_id: s
            for s in RunStatusService().all()
        }

        runs = []

        for item in history:

            status = statuses.get(item.id)

            runs.append(
                {
                    "id": item.id,
                    "name": f"Run {item.id[:8]}",
                    "created_at": item.created_at.isoformat(),
                    "experiments": item.experiments,
                    "status": status.status if status else "completed",
                    "progress": status.progress if status else 100,
                    "current_model": status.current_model if status else None,
                    "current_prompt": status.current_prompt if status else None,
                    "current_test_case": status.current_test_case if status else None,
                }
            )

        existing_ids = {r["id"] for r in runs}

        for status in statuses.values():

            if status.run_id in existing_ids:
                continue

            runs.insert(
                0,
                {
                    "id": status.run_id,
                    "name": f"Run {status.run_id[:8]}",
                    "created_at": (
                        status.started_at.isoformat()
                        if status.started_at
                        else ""
                    ),
                    "experiments": 0,
                    "status": status.status,
                    "progress": status.progress,
                    "current_model": status.current_model,
                    "current_prompt": status.current_prompt,
                    "current_test_case": status.current_test_case,
                },
            )

        runs.sort(
            key=lambda x: x["created_at"],
            reverse=True,
        )

        return runs