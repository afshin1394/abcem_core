from abc import abstractmethod
from typing import List

from app.domain.entities.walk_test_domain import WalkTestDomain


class WalkTestRepository:
    @abstractmethod
    async def save(self, walk_test_domain : WalkTestDomain) -> None:
        pass

    @abstractmethod
    async def get_all(self) -> List[WalkTestDomain]:
        pass
