from fastapi import APIRouter

from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/")
def dashboard():

    return DashboardService().get()