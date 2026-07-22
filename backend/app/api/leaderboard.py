from fastapi import APIRouter

from app.services.leaderboard_service import LeaderboardService

router = APIRouter(
    prefix="/api/leaderboard",
    tags=["Leaderboard"],
)


@router.get("")
def leaderboard():

    return LeaderboardService().list()