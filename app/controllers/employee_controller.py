from typing import List, Tuple

from sqlalchemy.orm import Session

from app import datastructures
from app.controllers import city_controller
from app.db.models.employee_location import EmployeeLocation


def update_employee_location(
    employee_form: datastructures.EmployeeForm, db_session: Session
) -> None:
    """Updates the employee's location. If the latitude and longitude cannot be found"""
    city_coordinates = city_controller.get_city_coordinates(employee_form.city)
    employee = EmployeeLocation(
        email=employee_form.email,
        city=employee_form.city,
        latitude=city_coordinates.lat,
        longitude=city_coordinates.lng,
    )
    db_session.add(employee)


def get_employee_current_locations(
    db_session: Session,
) -> List[datastructures.EmployeeLocation]:
    # TODO: Optimize: Do all in one query!
    employee_locations: List[datastructures.EmployeeLocation] = []
    email_addresses: List[Tuple[str]] = (
        db_session.query(EmployeeLocation.email).group_by(EmployeeLocation.email).all()
    )
    for (email,) in email_addresses:
        employee_location = (
            db_session.query(EmployeeLocation)
            .filter_by(email=email)
            .order_by(EmployeeLocation.inserted_at.desc())
            .limit(1)
            .first()
        )
        coordinates = datastructures.Coordinates(
            lat=employee_location.latitude, lng=employee_location.longitude
        )
        employee_locations.append(
            datastructures.EmployeeLocation(
                email=employee_location.email,
                city=employee_location.city,
                reported_at=employee_location.inserted_at,
                coordinates=coordinates,
            )
        )
    return employee_locations
