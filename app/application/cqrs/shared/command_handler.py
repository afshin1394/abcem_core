# ir/irancell/application/shared/command_handler.py

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from app.domain.events.event import Event


# Define a base Command class if not already defined
class Command:
    pass


# Define Type Variables with bounds
C = TypeVar('C', bound=Command)
E = TypeVar('E', bound=Event)


class CommandHandler(ABC, Generic[C, E]):
    """
    Abstract base class for handling commands and producing events.

    Args:
        C: A type variable bound to a Command subclass.
        E: A type variable bound to an Event subclass or None.
    """

    @abstractmethod
    async def handle(self, command: C) -> Optional[E]:
        """
        Handle the given command and optionally produce an event.

        Args:
            command (C): The command to handle.

        Returns:
            Optional[E]: The resulting event or None.
        """
        pass
