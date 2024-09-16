"""Submodule defining the company model."""

from sqlalchemy import Column, Integer, String

from app.database import Base


class Company(Base):
    """Model defining a company in the database."""

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    location = Column(String, nullable=False)
