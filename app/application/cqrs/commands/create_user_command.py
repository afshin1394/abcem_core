from app.application.cqrs.shared.command import Command


class CreateUserCommand(Command):
    name: str
    age: int
    gender: str
