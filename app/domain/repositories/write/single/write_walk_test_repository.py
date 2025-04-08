from abc import ABC, abstractmethod

from app.domain.entities.walk_test_domain import WalkTestDomain


class WriteWalkTestRepository(ABC):
    @abstractmethod
    async def create_walk_test(self,walk_test_domain : WalkTestDomain) -> None:
        pass
