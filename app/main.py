from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.core.loguru import setup_loguru


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_loguru()
    logger.info("App started, logs are working.")

    yield

    logger.info("App shutdown.")


app = FastAPI(lifespan=lifespan)
