from abc import ABC, abstractmethod
from typing import Tuple


class GetGISService(ABC):
    @abstractmethod
    async def get_haversine_distance(self,coord1: Tuple[float, float],
                               coord2: Tuple[float, float]) -> float:
        pass

    @abstractmethod
    async def are_all_locations_within_distance(self,coordinates : list[Tuple[float,float]],distance : float) -> bool:
        pass
