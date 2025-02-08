import uuid
from typing import Optional

from app.application.commands.create_user_command import CreateUserCommand
from app.application.shared.command_handler import CommandHandler, C, E
from app.domain.entities.users_domain import UserDomain
from app.domain.events.user_created_event import UserCreatedEvent
from app.domain.repositories.users_repository import UsersRepository


class CreateUserCommandHandler(CommandHandler):
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def handle(self, command: CreateUserCommand) -> UserCreatedEvent:
        await self.user_repository.save(UserDomain(name=command.name,age= command.age,gender=command.gender))


    async def deserialize_command(self, json_str: str) -> C:
        pass