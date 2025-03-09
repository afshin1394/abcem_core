from fastapi import Depends

from app.application.mediator import Mediator
from app.application.usecase.create_user_usecase import CreateUserUseCase
from app.application.usecase.create_walk_test_usecase import CreateWalkTestUseCase
from app.application.usecase.get_all_technology_types_usecase import GetAllTechnologyTypesUseCase
from app.application.usecase.get_all_walk_test_by_msisdn_usecase import GetAllWalkTestByMSISDNUseCase
from app.application.usecase.speed_test_server_list_usecase import SpeedTestServerListUseCase
from app.infrastructure.di.mediator import get_mediator
from app.infrastructure.di.usecases import get_create_user_use_case, get_speed_test_use_case, \
    get_create_walk_test_use_case, get_all_walk_test_by_msisdn_use_case, get_all_technology_type_use_case
from app.interfaces.controllers.authentication_controller import AuthenticationController
from app.interfaces.controllers.technology_type_controller import TechnologyTypeController
from app.interfaces.controllers.user_controller import UserController
from app.interfaces.controllers.walk_test_controller import WalkTestController


async def authentication_controller(mediator: Mediator = Depends(get_mediator)) -> AuthenticationController:
    return AuthenticationController(mediator=mediator)


async def get_create_user_controller(create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case),
                                     speed_test_server_list_use_case: SpeedTestServerListUseCase = Depends(
                                         get_speed_test_use_case)) -> UserController:
    return UserController(create_user_use_case=create_user_use_case,
                          speed_test_server_list_use_case=speed_test_server_list_use_case)


async def get_walk_test_controller(
        create_walk_test_use_case: CreateWalkTestUseCase = Depends(get_create_walk_test_use_case),
        get_walk_test_by_msisdn_use_case: GetAllWalkTestByMSISDNUseCase =
        Depends(get_all_walk_test_by_msisdn_use_case)) -> WalkTestController:
    return WalkTestController(
        create_walk_test_use_case=create_walk_test_use_case,
        get_all_walk_test_by_msisdn_use_case=get_walk_test_by_msisdn_use_case,
    )


async def get_technology_type_controller(technology_type_use_case: GetAllTechnologyTypesUseCase = Depends(get_all_technology_type_use_case)) -> TechnologyTypeController:
    return TechnologyTypeController(
        get_all_technology_types_use_case=technology_type_use_case
    )
