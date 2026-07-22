from fastapi import APIRouter

from app.services.dataset_service import DatasetService

router = APIRouter(
    prefix="/api/datasets",
    tags=["Datasets"],
)


@router.get("")
def datasets():

    return DatasetService().list()