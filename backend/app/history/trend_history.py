from app.history.run_history import RunHistory
from app.storage.run_repository import RunRepository


class TrendHistory:

    def load(self):

        history = RunHistory().load()

        runs = []
        names = []

        repository = RunRepository()

        # oldest → newest
        for item in reversed(history):

            runs.append(
                repository.load(item.path)
            )

            names.append(item.id)

        return runs, names