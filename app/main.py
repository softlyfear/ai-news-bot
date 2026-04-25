"""Application Entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.api.v1.api import router_v1
from app.core.database import get_async_engine
from app.core.database import get_async_session_factory
from app.core.loguru import setup_loguru
from app.crud.health import check_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI application lifespan."""

    setup_loguru()

    session_factory = get_async_session_factory()
    async with session_factory() as session:
        await check_database(session)

    logger.info("App started, logs are working.")

    try:
        yield
    finally:
        await get_async_engine().dispose()
        logger.info("Database engine disposed. App shutdown.")


app = FastAPI(lifespan=lifespan)

app.include_router(router_v1)
