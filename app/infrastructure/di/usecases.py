from app.application.mediator import Mediator
from app.application.usecase.create_user_usecase import CreateUserUseCase
from app.application.usecase.create_walk_test_usecase import CreateWalkTestUseCase
from app.application.usecase.get_all_complaint_types_usecase import GetAllComplaintTypesUseCase
from app.application.usecase.get_all_problematic_service_types_usecase import GetAllProblematicServiceTypesUseCase
from app.application.usecase.get_all_service_type_usecase import GetAllServiceTypeUseCase
from app.application.usecase.get_all_technology_type_usecase import GetAllTechnologyTypesUseCase
from app.application.usecase.get_all_test_step_type_usecase import GetAllTestStepTypeUseCase
from app.application.usecase.get_all_walk_test_by_msisdn_usecase import GetAllWalkTestByMSISDNUseCase
from app.application.usecase.speed_test_server_list_usecase import SpeedTestServerListUseCase
from app.domain.cache.cache_gateway import CacheGateway
from app.domain.repositories.speed_test_repository import SpeedTestRepository
from fastapi import Depends
from app.infrastructure.di.mediator import get_mediator
from app.infrastructure.di.redis_client import get_cache
from app.infrastructure.di.repositories import get_speed_test_repository


async def get_speed_test_use_case(
        speed_test_repository: SpeedTestRepository = Depends(get_speed_test_repository),
) -> SpeedTestServerListUseCase:
    return SpeedTestServerListUseCase(repository=speed_test_repository)


async def get_create_user_use_case(
        mediator: Mediator = Depends(get_mediator),
) -> CreateUserUseCase:
    return CreateUserUseCase(mediator=mediator)


async def get_create_walk_test_use_case(
        mediator: Mediator = Depends(get_mediator), cache_gateway: CacheGateway = Depends(get_cache)
) -> CreateWalkTestUseCase:
    return CreateWalkTestUseCase(mediator=mediator, cache_gateway=cache_gateway)


async def get_all_walk_test_by_msisdn_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllWalkTestByMSISDNUseCase:
    return GetAllWalkTestByMSISDNUseCase(mediator=mediator)


async def get_all_technology_type_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllTechnologyTypesUseCase:
    return GetAllTechnologyTypesUseCase(mediator=mediator)


async def get_all_complaint_type_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllComplaintTypesUseCase:
    return GetAllComplaintTypesUseCase(mediator=mediator)


async def get_all_problematic_service_type_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllProblematicServiceTypesUseCase:
    return GetAllProblematicServiceTypesUseCase(mediator=mediator)


async def get_all_service_type_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllServiceTypeUseCase:
    return GetAllServiceTypeUseCase(mediator=mediator)

async def get_all_test_step_type_use_case(
        mediator: Mediator = Depends(get_mediator)
) -> GetAllTestStepTypeUseCase:
    return GetAllTestStepTypeUseCase(mediator=mediator)