from fastapi import FastAPI

import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger
from typing import AsyncGenerator
from contextlib import asynccontextmanager



def create_base_app(configs):
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[dict, None]:
        """Управление жизненным циклом приложения."""
        logger.info("Инициализация приложения...")
        yield
        logger.info("Завершение работы приложения...")


    app = FastAPI(
        title=configs.PROJECT_NAME,
        lifespan=lifespan,
        description=configs.PROJECT_DESCRIPTION

    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.get("/")
    def root():
        return {"message": "Запустилось и работает!"}

    return  app
