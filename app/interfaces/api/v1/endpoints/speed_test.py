
from fastapi import APIRouter, Depends

from app.infrastructure.di.controllers import get_speed_test_servers_controller
from app.interfaces.controllers.speed_test_controller import SpeedTestServerController
from app.interfaces.dto.request.update_speed_test_servers_request import UpdateSpeedTestServersRequest
from app.interfaces.dto.success_response import BaseSuccessResponse

router_v1 = APIRouter(
    prefix="/speed_test",
    tags=["speed_test"],
)

@router_v1.post("/update_servers", response_model = BaseSuccessResponse)
async def update_servers(update_speed_test_servers_request : UpdateSpeedTestServersRequest, speed_test_controller : SpeedTestServerController = Depends(get_speed_test_servers_controller)) :
    return await speed_test_controller.update_speed_test_servers(update_speed_test_server_request=update_speed_test_servers_request)
