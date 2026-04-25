"""Health check CRUD operations."""

from loguru import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def check_database(session: AsyncSession) -> bool:
    """Check DB healthy."""

    try:
        await session.execute(text("SELECT 1"))
        logger.info("DB is OK.")
        return True
    except Exception as e:
        logger.error(f"DB Health check failed: {e}")
        return False
