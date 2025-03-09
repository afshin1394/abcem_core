from fastapi import Depends

from app.application.cqrs.commands.authenticate_command import AuthenticateCommand
from app.application.cqrs.commands.create_user_command import CreateUserCommand
from app.application.cqrs.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.cqrs.handlers.command_handler.authenticate_command_handler import AuthenticateCommandHandler
from app.application.cqrs.handlers.command_handler.create_user_command_handler import CreateUserCommandHandler
from app.application.cqrs.handlers.command_handler.create_walk_test_command_handler import CreateWalkTestCommandHandler
from app.application.cqrs.handlers.query_handler.get_walk_test_by_msisdn_query_handler import \
    GetWalkTestByMSISDNQueryHandler
from app.application.cqrs.queries.get_walk_test_by_msisdn_query import GetWalkTestByMSISDNQuery
from app.application.mediator import Mediator
from app.domain.repositories.users_repository import UsersRepository
from app.domain.services.get_ip_info_service import GetIpInfoService
from app.infrastructure.di.repositories import get_users_repository, get_read_walk_test_repository, \
    get_write_walk_test_repository

from app.infrastructure.di.services import get_ip_info_service


def get_mediator(get_ip_info_service: GetIpInfoService = Depends(get_ip_info_service),
                 users_repository: UsersRepository = Depends(get_users_repository),
                 read_walk_test_repository=Depends(get_read_walk_test_repository),
                 write_walk_test_repository=Depends(get_write_walk_test_repository)
                 ) -> Mediator:
    # commands

    mediator = Mediator()
    # Register command handlers
    mediator.register_handler(AuthenticateCommand, AuthenticateCommandHandler(get_ip_info_service).handle)
    # Register query handlers
    mediator.register_handler(CreateUserCommand, CreateUserCommandHandler(users_repository).handle)

    mediator.register_handler(CreateWalkTestCommand, CreateWalkTestCommandHandler(write_walk_test_repository).handle)

    # queries
    mediator.register_handler(GetWalkTestByMSISDNQuery,
                              GetWalkTestByMSISDNQueryHandler(read_walk_test_repository).handle)

    return mediator
