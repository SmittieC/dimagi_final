from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from app.db.base import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    city = Column(String, nullable=False)
    # If we can't determine the lat/lng, at least we have the city to go with
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)

    # If no datetime inserted, we assume
    inserted_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(tz=timezone.utc),
    )
