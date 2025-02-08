from fastapi import APIRouter

from .endpoints.validation.validation import router_v1 as validation_router
from .endpoints.authentication.authentication import router_v1 as authentication_router

router_v1 = APIRouter()

router_v1.include_router(validation_router)
router_v1.include_router(authentication_router)