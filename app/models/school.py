"""Submodule defining the school model."""

from sqlalchemy import Column, Integer, String

from app.database import Base


class School(Base):
    """Model defining a school in the database."""

    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    location = Column(String, nullable=False)
