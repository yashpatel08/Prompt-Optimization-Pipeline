from fastapi import APIRouter

from app.services.compare_service import CompareService

router = APIRouter(
    prefix="/api/compare",
    tags=["Compare"],
)


@router.get("/options")
def compare_options():

    return CompareService().options()


@router.get("")
def compare(
    left: str,
    right: str,
):

    return CompareService().compare(
        left,
        right,
    )