# tests/use_cases/test_distance_calculator.py

import pytest
from typing import Tuple, List
from app.infrastructure.repository_impl.get_gis_repository_impl import GetGISServiceImpl


@pytest.fixture
def gis_repository():
    """
    Fixture to instantiate the GetGISRepositoryImpl.
    """
    return GetGISServiceImpl()


def test_empty_coordinates(gis_repository: GetGISServiceImpl):
    """
    Test that an empty list of coordinates returns True.
    """
    coordinates: List[Tuple[float, float]] = []
    assert gis_repository.are_all_locations_within_distance(coordinates) is True


def test_single_coordinate(gis_repository: GetGISServiceImpl):
    """
    Test that a single coordinate returns True.
    """
    coordinates: List[Tuple[float, float]] = [(40.748817, -73.985428)]
    assert gis_repository.are_all_locations_within_distance(coordinates) is True


def test_all_within_distance(gis_repository: GetGISServiceImpl):
    """
    Test that all coordinates are within the specified distance.
    """
    coordinates: List[Tuple[float, float]] = [
        (40.748817, -73.985428),  # Empire State Building
        (40.748900, -73.985500),  # Very close
        (40.748700, -73.985300)   # Very close
    ]
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is True


def test_some_exceed_distance(gis_repository: GetGISServiceImpl):
    """
    Test that the function returns False when at least one pair exceeds the specified distance.
    """
    coordinates: List[Tuple[float, float]] = [
        (40.748817, -73.985428),  # Empire State Building
        (40.758896, -73.985130),  # Times Square (~1100 meters away)
        (40.748700, -73.985300)   # Very close
    ]
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is False


def test_boundary_distance(gis_repository: GetGISServiceImpl):
    """
    Test coordinates that are exactly at the boundary distance.
    """
    # Coordinates approximately 50 meters apart
    coordinates: List[Tuple[float, float]] = [
        (40.748817, -73.985428),
        (40.749267, -73.985428)  # ~50 meters north
    ]
    # Allow a small epsilon for floating point precision
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is True


def test_identical_coordinates(gis_repository: GetGISServiceImpl):
    """
    Test multiple identical coordinates, should return True.
    """
    coordinates: List[Tuple[float, float]] = [
        (40.748817, -73.985428),
        (40.748817, -73.985428),
        (40.748817, -73.985428)
    ]
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is True


def test_invalid_coordinates_non_numeric(gis_repository: GetGISServiceImpl):
    """
    Test that non-numeric coordinates raise a ValueError.
    """
    coordinates: List[Tuple[float, float]] = [
        ("40.748817", "-73.985428"),  # Strings instead of floats
        (40.748900, -73.985500)
    ]
    with pytest.raises(ValueError) as exc_info:
        gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0)
    assert "Invalid coordinate format" in str(exc_info.value)


def test_invalid_coordinates_incomplete_tuple(gis_repository: GetGISServiceImpl):
    """
    Test that coordinates with incomplete tuples raise a ValueError.
    """
    coordinates: List[Tuple[float, float]] = [
        (40.748817,),  # Incomplete tuple
        (40.748900, -73.985500)
    ]
    with pytest.raises(ValueError) as exc_info:
        gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0)
    assert "Invalid coordinate format" in str(exc_info.value)


def test_large_dataset_all_within_distance(gis_repository: GetGISServiceImpl):
    """
    Test a large number of coordinates all within the specified distance.
    """
    base_lat, base_lon = 40.748817, -73.985428
    num_points = 100
    # Slight variations within ~50 meters
    # Approximately 0.00045 degrees is ~50 meters
    coordinates: List[Tuple[float, float]] = [
        (base_lat + 0.00045 * (i % 10), base_lon + 0.00045 * (i % 10)) for i in range(num_points)
    ]
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is True


def test_large_dataset_some_exceed_distance(gis_repository: GetGISServiceImpl):
    """
    Test a large number of coordinates where some pairs exceed the specified distance.
    """
    base_lat, base_lon = 40.748817, -73.985428
    num_points = 100
    # Slight variations within ~50 meters
    coordinates: List[Tuple[float, float]] = [
        (base_lat + 0.00045 * (i % 10), base_lon + 0.00045 * (i % 10)) for i in range(num_points)
    ]
    # Add a distant point (~1100 meters away)
    coordinates.append((40.758896, -73.985130))  # Times Square
    assert gis_repository.are_all_locations_within_distance(coordinates, max_distance=50.0) is False
