from fastapi import APIRouter

from src.presentation.rest.sms.router import sms_router

# ---------------------------------------------------------------------------
router = APIRouter()

# ---------------------------------------------------------------------------
router.include_router(sms_router, prefix="/sms", tags=["SMS Service"])
