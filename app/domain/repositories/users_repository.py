
from abc import  abstractmethod
from typing import List

from app.domain.entities.users_domain import UserDomain


class UsersRepository:
    @abstractmethod
    async def save(self, userDomain : UserDomain) -> None:
        pass

    @abstractmethod
    async def get_all(self) -> List[UserDomain]:
        pass

