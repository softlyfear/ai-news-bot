"""All v1 API routers."""

from fastapi import APIRouter

from app.api.v1.endpoints.health import root_router as root_router
from app.api.v1.endpoints.health import router as health_router

router_v1 = APIRouter()

router_v1.include_router(root_router, tags=["health"])
router_v1.include_router(health_router, prefix="/health", tags=["health"])
