"""Enum source type and status."""

from enum import StrEnum


class SourceType(StrEnum):
    """News source."""

    site = "site"
    tg = "tg"
    x = "x"


class PostStatus(StrEnum):
    """Post status."""

    new = "new"
    generated = "generated"
    published = "published"
    failed = "failed"
