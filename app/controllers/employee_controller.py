from geocoder import geonames
from sqlalchemy.orm import Session

from app.config import Config
from app.datastructures import Coordinates, EmployeeForm
from app.db.models.employee import Employee


def update_employee_location(employee_form: EmployeeForm, db_session: Session) -> None:
    city_coordinates = get_city_coordinates(employee_form.city)
    employee = Employee(
        email=employee_form.email,
        city=employee_form.city,
        latitude=city_coordinates.lat,
        longitude=city_coordinates.lng,
    )
    db_session.add(employee)


def get_city_coordinates(city_name: str) -> Coordinates:
    """Query the geo-service to find the city's lat and lng"""
    # TODO: Improve: Store local copy of this info and query database rather
    city_details = geonames(city_name, key=Config.GEOCODER_API_KEY)
    return Coordinates(lat=city_details.lat, lng=city_details.lng)
