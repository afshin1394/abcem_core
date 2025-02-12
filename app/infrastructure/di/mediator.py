from fastapi import Depends

from app.application.commands.authenticate_command import AuthenticateCommand
from app.application.commands.create_user_command import CreateUserCommand
from app.application.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.handlers.authenticate_command_handler import AuthenticateCommandHandler
from app.application.handlers.create_user_command_handler import CreateUserCommandHandler
from app.application.handlers.create_walk_test_command_handler import CreateWalkTestCommandHandler
from app.application.mediator import Mediator
from app.domain.repositories.users_repository import UsersRepository
from app.domain.services.get_ip_info_service import GetIpInfoService
from app.infrastructure.di.repositories import get_users_repository, get_walk_test_repository
from app.infrastructure.di.services import get_ip_info_service

def get_mediator(get_ip_info_service : GetIpInfoService = Depends(get_ip_info_service),
                 users_repository : UsersRepository = Depends(get_users_repository),
                 walk_test_repository = Depends(get_walk_test_repository)
                 ) -> Mediator:
    mediator = Mediator()
    # Register command handlers
    mediator.register_handler(AuthenticateCommand, AuthenticateCommandHandler(get_ip_info_service).handle)
    # Register query handlers
    mediator.register_handler(CreateUserCommand, CreateUserCommandHandler(users_repository).handle)

    mediator.register_handler(CreateWalkTestCommand, CreateWalkTestCommandHandler(walk_test_repository).handle)

    return mediator