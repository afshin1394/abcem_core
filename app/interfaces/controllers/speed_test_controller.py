from app.application.usecase.update_speed_test_server_use_case import UpdateSpeedTestServersUseCase
from app.interfaces.dto.request.update_speed_test_servers_request import UpdateSpeedTestServersRequest
from app.interfaces.dto.response.speed_test_server_response import SpeedTestsServersResponse


class SpeedTestServerController:

    def __init__(self, update_speed_test_server_use_case: UpdateSpeedTestServersUseCase) -> None:
        self.update_speed_test_server_use_case = update_speed_test_server_use_case

    async def update_speed_test_servers(self,update_speed_test_server_request: UpdateSpeedTestServersRequest) -> None:

         await self.update_speed_test_server_use_case(update_speed_test_server_request = update_speed_test_server_request)
         return SpeedTestsServersResponse(status_code = 204,result= None)