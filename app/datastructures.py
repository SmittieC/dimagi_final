from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class EmployeeForm(BaseModel):
    email: str  # get validator
    city: str


class Coordinates(BaseModel):
    lat: Optional[str] = Field(default=None)
    lng: Optional[str] = Field(default=None)


class EmployeeLocation(BaseModel):
    email: str
    city: str
    reported_at: datetime
    coordinates: Coordinates
