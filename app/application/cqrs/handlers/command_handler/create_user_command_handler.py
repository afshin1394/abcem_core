from app.application.cqrs.commands.create_user_command import CreateUserCommand
from app.application.cqrs.shared.command_handler import CommandHandler, C
from app.domain.entities.users_domain import UserDomain
from app.domain.events.user_created_event import UserCreatedEvent
from app.domain.repositories.users_repository import UsersRepository


class CreateUserCommandHandler(CommandHandler[CreateUserCommand, UserCreatedEvent]):
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def handle(self, command: CreateUserCommand) -> UserCreatedEvent:
        return await self.user_repository.save(UserDomain(name=command.name, age=command.age, gender=command.gender))

