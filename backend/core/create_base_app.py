
from fastapi import FastAPI

import logging


def create_base_app(configs):

    logging.basicConfig(level=logging.INFO)

    app = FastAPI(
        title=configs.PROJECT_NAME,
        openapi_url=f"{configs.API}/openapi.json",
        version="0.0.1",
        description="Апихи для хакатона ЛЦТ"

    )

    @app.get("/")
    def root():
        return configs.PROJECT_NAME + " Работает"

    @app.get("/sentry-debug")
    async def trigger_error():
        division_by_zero = 1 / 0

    @app.get("/sentry-logging")
    async def trigger_error():
        logging.info('logging Работает')

    return app



