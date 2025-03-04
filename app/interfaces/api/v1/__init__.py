from fastapi import APIRouter

from app.interfaces.api.v1.endpoints.validation import router_v1 as validation_router
from app.interfaces.api.v1.endpoints.authentication import router_v1 as authentication_router
from app.interfaces.api.v1.endpoints.walk_test import router_v1 as walk_test_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(validation_router)
router_v1.include_router(authentication_router)

router_v1.include_router(walk_test_router)