# app/application/mediator.py
from typing import Type, Callable, Dict, Any
from inspect import iscoroutinefunction
import logging


class Mediator:
    def __init__(self):
        self._handlers: Dict[Type, Callable[[Any], Any]] = {}

    def register_handler(self, message_type: Type, handler: Callable[[Any], Any]):
        self._handlers[message_type] = handler

    async def send(self, message: Any = None) -> Any:
        logging.debug("\nsend\n")
        message_type = type(message)
        handler = self._handlers.get(message_type)
        if not handler:
            raise ValueError(f"No handler registered for {message_type}")
        if iscoroutinefunction(handler):
            return await handler(message)
        else:
            return handler(message)
