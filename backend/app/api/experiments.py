from fastapi import APIRouter
from fastapi import BackgroundTasks
import uuid
from app.datasets.loader import DatasetLoader
from app.prompts import prompts
from app.model_registry import models
from app.experiment_runner import ExperimentRunner
from app.models.run import Run
from app.storage.run_repository import RunRepository
from app.services.run_status_service import RunStatusService
from app.services.experiment_service import ExperimentService

router = APIRouter(prefix="/api/experiments", tags=["Experiments"])

@router.get("")
def experiments():

    return ExperimentService().list()

@router.post("/run")
def run_experiments(background_tasks: BackgroundTasks):

    run_id = str(uuid.uuid4())

    background_tasks.add_task(
        execute_run,
        run_id,
    )

    return {
        "status": "started",
        "run_id": run_id,
    }


def execute_run(run_id: str):

    dataset = DatasetLoader().load("datasets/qa.json")

    runner = ExperimentRunner(
        prompts=prompts,
        dataset=dataset,
        models=models,
    )

    RunStatusService().create(run_id)
    experiments = runner.run()

    run = Run(experiments)

    RunRepository().save(run)

@router.get("/{run_id}/status")
def run_status(run_id: str):

    status = RunStatusService().get(run_id)

    if status is None:
        return {
            "error": "Run not found"
        }

    return status