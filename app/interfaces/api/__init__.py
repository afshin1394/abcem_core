from fastapi import APIRouter

from .v1 import router_v1 as v1
from .v2 import router_v2  as v2

router_all = APIRouter()

router_all.include_router(v1, prefix="/v1",tags=["v1"])
router_all.include_router(v2, prefix="/v2",tags=["v2"])
