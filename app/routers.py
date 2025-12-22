from fastapi import APIRouter
from app.routers.health import router as health_router
from app.routers.items import router as items_router

router = APIRouter()
router.include_router(health_router)
router.include_router(items_router)
