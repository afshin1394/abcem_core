from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.walk_test_domain import WalkTestDomain


class ReadWalkTestRepository(ABC):
    @abstractmethod
    async def get_all_by_msisdn(self, msisdn: str) -> List[WalkTestDomain]:
        raise NotImplementedError
