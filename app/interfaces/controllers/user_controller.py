from typing import List

from app.application.usecase.create_user_usecase import CreateUserUseCase
from app.application.usecase.speed_test_server_list_usecase import SpeedTestServerListUseCase
from app.interfaces.dto.request.user_create_request import CreateUserRequest
from fastapi import logger

from app.interfaces.dto.response.server_response import SpeedTestServerResponse
from app.interfaces.mapper.speed_test_server_mapper import response_list_from_domain_list


class UserController:

    def __init__(self,create_user_use_case : CreateUserUseCase,speed_test_server_list_use_case: SpeedTestServerListUseCase):
          self.create_user_use_case = create_user_use_case
          self.speed_test_server_list_use_case = speed_test_server_list_use_case

    async  def create_user(self, create_user_request : CreateUserRequest)->str:
        logger.logger.debug(msg=f'create_user {create_user_request.__str__()}')
        logger.logger.debug(msg=f'create_user {self.create_user_use_case.__str__()}')
        await self.create_user_use_case.execute(create_user_request= create_user_request)
        return "string"

    async def speed_test_init(self)->List[SpeedTestServerResponse]:
        return response_list_from_domain_list((await self.speed_test_server_list_use_case.execute(concurrency= 1 ,retries=3)))