from unittest import TestCase

from mock import patch

from app.controllers.employee_controller import update_employee_location
from app.datastructures import Coordinates, EmployeeForm
from app.db.base import session_scope
from app.db.models.employee_location import EmployeeLocation


def _employee_form() -> EmployeeForm:
    return EmployeeForm(city="Cape Town", email="someone@example.com")


@patch("app.controllers.employee_controller.city_controller")
def test_update_employee_location_success(mock_city_controller):
    employee_form = _employee_form()
    expected_lat = "-14.123"
    expected_lng = "-12.123"
    mock_city_controller.get_city_coordinates.return_value = Coordinates(
        lat=expected_lat, lng=expected_lng
    )

    with session_scope() as db_session:
        update_employee_location(employee_form=employee_form, db_session=db_session)

    with session_scope() as db_session:
        created_employee_location = (
            db_session.query(EmployeeLocation)
            .filter_by(email=employee_form.email)
            .order_by(EmployeeLocation.inserted_at.desc())
            .first()
        )
        assert created_employee_location.city == employee_form.city
        assert created_employee_location.inserted_at is not None
        assert created_employee_location.latitude == expected_lat
        assert created_employee_location.longitude == expected_lng


@patch("app.controllers.employee_controller.city_controller")
def test_update_employee_location_success_without_location_data(mock_city_controller):
    employee_form = _employee_form()
    mock_city_controller.get_city_coordinates.return_value = Coordinates()

    with session_scope() as db_session:
        update_employee_location(employee_form=employee_form, db_session=db_session)

    with session_scope() as db_session:
        created_employee_location = (
            db_session.query(EmployeeLocation)
            .filter_by(email=employee_form.email)
            .order_by(EmployeeLocation.inserted_at.desc())
            .first()
        )
        assert created_employee_location.city == employee_form.city
        assert created_employee_location.inserted_at is not None
        assert created_employee_location.latitude == None
        assert created_employee_location.longitude == None
