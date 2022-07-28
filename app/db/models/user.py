from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.models.pet import Pet


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    pets = relationship(
        "Pet",
        order_by=Pet.id,
        back_populates="user",
        cascade="all, delete, delete-orphan",
    )
