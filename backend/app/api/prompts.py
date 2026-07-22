from fastapi import APIRouter

from app.services.prompt_service import PromptService

router = APIRouter(
    prefix="/api/prompts",
    tags=["Prompts"],
)


@router.get("")
def prompts():

    return PromptService().list()