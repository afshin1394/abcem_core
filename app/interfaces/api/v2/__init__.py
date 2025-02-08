from fastapi import APIRouter, Depends

from .endpoints.validation.validation import router_v2 as validation_router
from .endpoints.authentication.authentication import router_v2 as authentication_router

router_v2 = APIRouter()

router_v2.include_router(validation_router)
router_v2.include_router(authentication_router)