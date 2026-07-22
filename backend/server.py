from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.experiments import router as experiments_router
from app.api.dashboard import router as dashboard_router
from app.api.prompts import router as prompts_router
from app.api.datasets import router as datasets_router
from app.api.leaderboard import router as leaderboard_router
from app.api.compare import router as compare_router

app = FastAPI(
    title="PromptOps",
    version="1.0.0",
)

origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"],  
)

app.include_router(experiments_router)
app.include_router(dashboard_router)
app.include_router(prompts_router)
app.include_router(datasets_router)
app.include_router(leaderboard_router)
app.include_router(compare_router)