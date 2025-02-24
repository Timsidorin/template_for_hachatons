
from fastapi import FastAPI

import logging


def create_base_app(configs):

    logging.basicConfig(level=logging.INFO)

    app = FastAPI(
        title=configs.PROJECT_NAME,
        version="0.0.1",
        description="Апихи для хакатона ЛЦТ"

    )

    @app.get("/")
    def root():
        return configs.PROJECT_NAME + " Работает"



