"""Healths pydantic models."""

from pydantic import BaseModel


class RootResponse(BaseModel):
    """Root directory model."""

    service: str
    status: str
    version: str


class LiveResponse(BaseModel):
    """Live response model."""

    status: str
