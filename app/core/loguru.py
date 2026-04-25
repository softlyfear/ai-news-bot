"""Loguru settings."""

import sys
from functools import lru_cache

from loguru import logger

from app.core.config import get_settings

settings = get_settings()


@lru_cache(maxsize=1)
def setup_loguru():
    """Logger configuration."""

    logger.remove()

    logger.add(
        sys.stderr,
        level=settings.log.LEVEL_CONSOLE,
        colorize=True,
        backtrace=settings.log.BACKTRACE,
        diagnose=settings.log.DIAGNOSE,
    )

    logger.add(
        settings.log.FILE_PATH,
        level=settings.log.LEVEL_FILE,
        rotation=settings.log.ROTATION,
        retention=settings.log.RETENTION,
        enqueue=settings.log.ENQUEUE,
        serialize=settings.log.JSON,
        backtrace=settings.log.BACKTRACE,
        diagnose=settings.log.DIAGNOSE,
    )
