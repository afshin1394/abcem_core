import math
from typing import Tuple, List

from app.domain.services.get_gis_service import GetGISService


class GetGISServiceImpl(GetGISService):
    def __init__(self):
        pass

    def get_haversine_distance(
        self, coord1: Tuple[float, float], coord2: Tuple[float, float]
    ) -> float:
        """
        Calculate the great-circle distance between two points on the Earth
        specified by their latitude and longitude using the Haversine formula.

        Parameters:
            coord1: Tuple containing latitude and longitude of the first point in decimal degrees.
            coord2: Tuple containing latitude and longitude of the second point in decimal degrees.

        Returns:
            Distance between the two points in meters.
        """

        # Radius of the Earth in meters
        R = 6371000

        lat1_rad = math.radians(coord1[0])
        lat2_rad = math.radians(coord2[0])
        delta_lat_rad = math.radians(coord2[0] - coord1[0])
        delta_lon_rad = math.radians(coord2[1] - coord1[1])

        a = (
            math.sin(delta_lat_rad / 2) ** 2
            + math.cos(lat1_rad)
            * math.cos(lat2_rad)
            * math.sin(delta_lon_rad / 2) ** 2
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def are_all_locations_within_distance(
        self, coordinates: List[Tuple[float, float]], max_distance: float = 50.0
    ) -> bool:
        """
        Check whether all locations in the list are within the specified distance of each other.

        Parameters:
            coordinates: List of tuples, where each tuple contains latitude and longitude in decimal degrees.
            max_distance: Maximum allowed distance in meters between any two locations (default is 50 meters).

        Returns:
            True if all locations are within max_distance of each other, False otherwise.
        """
        num_locations = len(coordinates)

        # Edge cases
        if num_locations <= 1:
            return True  # Single location or empty list is trivially within any distance

        # Compare each pair only once
        for i in range(num_locations):
            for j in range(i + 1, num_locations):
                distance = self.get_haversine_distance(coordinates[i], coordinates[j])
                if distance > max_distance:
                    print(
                        f"Distance between {coordinates[i]} and {coordinates[j]} is {distance:.2f} meters, which exceeds {max_distance} meters."
                    )
                    return False
                else:
                    print(
                        f"Distance between {coordinates[i]} and {coordinates[j]} is {distance:.2f} meters."
                    )

        return True
