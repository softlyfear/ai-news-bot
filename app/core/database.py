"""Database engine and session configuration."""

from collections.abc import AsyncGenerator
from functools import lru_cache

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import get_settings

settings = get_settings()


@lru_cache(maxsize=1)
def get_async_engine() -> AsyncEngine:
    """Create and cache async SQLAlchemy engine lazily."""

    return create_async_engine(
        url=settings.db.DATABASE_URL,
        echo=settings.db.ECHO,
        pool_size=settings.db.POOL_SIZE,
        max_overflow=settings.db.MAX_OVERFLOW,
        pool_pre_ping=settings.db.POOL_PRE_PING,
        pool_recycle=settings.db.POOL_RECYCLE,
    )


@lru_cache(maxsize=1)
def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
    """Create and cache async session factory lazily."""

    return async_sessionmaker(
        bind=get_async_engine(),
        autoflush=settings.db.AUTOFLUSH,
        expire_on_commit=settings.db.EXPIRE_ON_COMMIT,
    )


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    """Provide session with automatic commit on success and rollback on error."""

    session_factory = get_async_session_factory()

    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            logger.bind(
                error_type=type(e).__name__,
                operation="db_session",
            ).exception("Database session error")
            raise
