"""
Точка входа в backend
"""
#
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core.config import configs
from loguru import logger

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[dict, None]:
    """Управление жизненным циклом приложения."""
    logger.info("Инициализация приложения...")
    yield
    logger.info("Завершение работы приложения...")


app = FastAPI(lifespan=lifespan,
              title=configs.PROJECT_NAME
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home_page():
    return {"message": "Запустилось и работает!"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8006)
    # uvicorn.run("main:app", host="localhost", port=8000, reload=True)
