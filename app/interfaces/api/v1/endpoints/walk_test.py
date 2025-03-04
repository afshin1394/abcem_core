from fastapi import APIRouter,Depends

from app.infrastructure.di.controllers import get_walk_test_controller
from app.interfaces.controllers.walk_test_controller import WalkTestController
from app.interfaces.dto.request.walk_test_request import WalkTestRequest

router_v1 = APIRouter(
    prefix="/walk_test",
    tags=["walk_test"]
)


@router_v1.post("/create")
async def validate_location(walk_test_request : WalkTestRequest,walk_test_controller : WalkTestController = Depends(get_walk_test_controller)):
    return await walk_test_controller.create_walk_test(walk_test_request)