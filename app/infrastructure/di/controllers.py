from fastapi import Depends

from app.application.mediator import Mediator
from app.application.usecase.create_user_usecase import CreateUserUseCase
from app.application.usecase.speed_test_server_list_usecase import SpeedTestServerListUseCase
from app.infrastructure.di.mediator import get_mediator
from app.infrastructure.di.usecases import get_create_user_use_case, get_speed_test_use_case
from app.interfaces.controllers.authentication_controller import AuthenticationController
from app.interfaces.controllers.user_controller import UserController


async def authentication_controller(mediator: Mediator = Depends(get_mediator)) -> AuthenticationController:
    return AuthenticationController(mediator = mediator)


async def get_create_user_controller(create_user_use_case : CreateUserUseCase = Depends(get_create_user_use_case),speed_test_server_list_use_case : SpeedTestServerListUseCase = Depends(get_speed_test_use_case)) -> UserController:
    return  UserController(create_user_use_case = create_user_use_case,speed_test_server_list_use_case = speed_test_server_list_use_case)
