"""Health API endpoints."""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from app.core.config import get_settings
from app.core.deps import SessionDep
from app.crud.health import check_database
from app.schemas.health import LiveResponse
from app.schemas.health import RootResponse

settings = get_settings()

router = APIRouter()
root_router = APIRouter()


@root_router.get(
    "/",
    response_model=RootResponse,
    status_code=status.HTTP_200_OK,
)
async def root() -> RootResponse:
    """Root page."""
    return RootResponse(
        service="Ai News Bot",
        status="running",
        version=settings.app.VERSION,
    )


@router.get(
    "/live",
    response_model=LiveResponse,
    status_code=status.HTTP_200_OK,
)
async def liveness() -> LiveResponse:
    """App status."""

    return LiveResponse(status="alive")


@router.get("/ready")
async def readiness(
    session: SessionDep,
) -> dict:
    """Checking dependencies."""

    db_ok = await check_database(session)
    if not db_ok:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "not_ready", "db_ok": False},
        )

    return {"status": "ready", "db_ok": True}
