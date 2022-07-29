import pytest
from mock import patch

from app.controllers.city_controller import get_city_coordinates
from app.datastructures import Coordinates
from app.exceptions import InvalidCityException


@patch("app.controllers.city_controller.geonames")
def test_get_city_coordinates_success(mock_geonames):
    class MockGeonamesQuery:
        ok: bool = True
        lat: str = "14"
        lng: str = "14"

    mock_geonames.return_value = MockGeonamesQuery()
    response = get_city_coordinates(city_name="Some city")
    assert isinstance(response, Coordinates)


@patch("app.controllers.city_controller.geonames")
def test_get_city_coordinates_raises_for_invalid_city(mock_geonames):
    class MockGeonamesQuery:
        ok: bool = False

    mock_geonames.return_value = MockGeonamesQuery()
    with pytest.raises(InvalidCityException):
        get_city_coordinates(city_name="Some city")
