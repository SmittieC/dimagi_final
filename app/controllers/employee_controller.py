from typing import List

from sqlalchemy.orm import Session

from app.controllers import city_controller
from app.datastructures import EmployeeForm, EmployeeLocation
from app.db.models import employee_location


def update_employee_location(employee_form: EmployeeForm, db_session: Session) -> None:
    city_coordinates = city_controller.get_city_coordinates(employee_form.city)
    employee = employee_location.EmployeeLocation(
        email=employee_form.email,
        city=employee_form.city,
        latitude=city_coordinates.lat,
        longitude=city_coordinates.lng,
    )
    db_session.add(employee)


def get_employee_current_locations(db_session: Session) -> List[EmployeeLocation]:
    employees = db_session.query(Employee.email)
    db_session.query(Employee).group_by(Employee.email).order_by(
        Employee.inserted_at.desc()
    ).all()
