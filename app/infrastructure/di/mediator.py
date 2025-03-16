from fastapi import Depends

from app.application.cqrs.commands.authenticate_command import AuthenticateCommand
from app.application.cqrs.commands.create_user_command import CreateUserCommand
from app.application.cqrs.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.cqrs.commands.update_device_info_command import UpdateDeviceInfoCommand
from app.application.cqrs.handlers.command_handler.authenticate_command_handler import AuthenticateCommandHandler
from app.application.cqrs.handlers.command_handler.create_user_command_handler import CreateUserCommandHandler
from app.application.cqrs.handlers.command_handler.create_walk_test_command_handler import CreateWalkTestCommandHandler
from app.application.cqrs.handlers.command_handler.update_device_info_command_handler import \
    UpdateDeviceInfoCommandHandler
from app.application.cqrs.handlers.query_handler.get_all_complaint_type_query_handler import \
    GetAllComplaintTypeQueryHandler
from app.application.cqrs.handlers.query_handler.get_all_problematic_service_type_query_handler import \
    GetAllProblematicServiceTypeQueryHandler
from app.application.cqrs.handlers.query_handler.get_all_service_type_query_handler import GetAllServiceTypeQueryHandler
from app.application.cqrs.handlers.query_handler.get_all_technology_types_query_handler import \
    GetAllTechnologyTypesQueryHandler
from app.application.cqrs.handlers.query_handler.get_all_test_step_type_query_handler import \
    GetAllTestStepTypeQueryHandler
from app.application.cqrs.handlers.query_handler.get_walk_test_by_msisdn_query_handler import \
    GetWalkTestByMSISDNQueryHandler
from app.application.cqrs.queries.get_all_complaint_type_query import GetAllComplaintTypeQuery
from app.application.cqrs.queries.get_all_problematic_service_type_query import GetAllProblematicServiceTypeQuery
from app.application.cqrs.queries.get_all_service_type_query import GetAllServiceTypeQuery
from app.application.cqrs.queries.get_all_technology_types_query import GetAllTechnologyTypesQuery
from app.application.cqrs.queries.get_all_test_step_type_query import GetAllTestStepTypeQuery
from app.application.cqrs.queries.get_walk_test_by_msisdn_query import GetWalkTestByMSISDNQuery
from app.application.mediator import Mediator
from app.domain.cache.cache_gateway import CacheGateway
from app.domain.repositories.users_repository import UsersRepository
from app.domain.services.get_ip_info_service import GetIpInfoService
from app.infrastructure.di.redis_client import get_cache
from app.infrastructure.di.repositories import get_users_repository, get_read_walk_test_repository, \
    get_write_walk_test_repository, get_read_technology_type_repository, get_read_complaint_type_repository, \
    get_read_problematic_service_type_repository, get_read_service_type_repository, get_read_test_step_type_repository, \
    get_write_device_info_repository

from app.infrastructure.di.services import get_ip_info_service


def get_mediator(
        cache_gateway : CacheGateway = Depends(get_cache),
        ip_info_service: GetIpInfoService = Depends(get_ip_info_service),
                 users_repository: UsersRepository = Depends(get_users_repository),
                 read_walk_test_repository=Depends(get_read_walk_test_repository),
                 write_walk_test_repository=Depends(get_write_walk_test_repository,),
                 write_device_info_repository = Depends(get_write_device_info_repository,),
                 read_technology_repository=Depends(get_read_technology_type_repository,),
                 read_complaint_type_repository = Depends(get_read_complaint_type_repository),
                 read_problematic_service_repository = Depends(get_read_problematic_service_type_repository),
                 read_service_type_repository = Depends(get_read_service_type_repository),
                 read_test_step_type_repository = Depends(get_read_test_step_type_repository),

) -> Mediator:
    # commands
    mediator = Mediator()
    mediator.register_handler(AuthenticateCommand, AuthenticateCommandHandler(ip_info_service,cache_gateway=cache_gateway))
    mediator.register_handler(CreateUserCommand, CreateUserCommandHandler(users_repository,cache_gateway=cache_gateway))
    mediator.register_handler(CreateWalkTestCommand, CreateWalkTestCommandHandler(write_walk_test_repository,cache_gateway=cache_gateway))
    mediator.register_handler(UpdateDeviceInfoCommand,UpdateDeviceInfoCommandHandler(write_device_info_repository= write_device_info_repository,cache_gateway=cache_gateway))

    # queries
    mediator.register_handler(GetWalkTestByMSISDNQuery,
                              GetWalkTestByMSISDNQueryHandler(read_walk_test_repository,cache_gateway=cache_gateway,expire=3600))
    mediator.register_handler(GetAllTechnologyTypesQuery,
                              GetAllTechnologyTypesQueryHandler(read_technology_repository,cache_gateway=cache_gateway,expire=3600))
    mediator.register_handler(GetAllComplaintTypeQuery,GetAllComplaintTypeQueryHandler(read_complaint_type_repository,cache_gateway=cache_gateway,expire=3600))
    mediator.register_handler(GetAllProblematicServiceTypeQuery,GetAllProblematicServiceTypeQueryHandler(read_problematic_service_repository,cache_gateway=cache_gateway,expire=3600))
    mediator.register_handler(GetAllServiceTypeQuery,GetAllServiceTypeQueryHandler(read_service_type_repository,cache_gateway=cache_gateway,expire=3600))
    mediator.register_handler(GetAllTestStepTypeQuery,GetAllTestStepTypeQueryHandler(read_test_step_type_repository,cache_gateway=cache_gateway,expire=3600))

    return mediator
