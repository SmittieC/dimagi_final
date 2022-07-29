from pydantic import BaseModel


class EmployeeForm(BaseModel):
    email: str  # get validator
    city: str


class Coordinates(BaseModel):
    lat: str
    lng: str
