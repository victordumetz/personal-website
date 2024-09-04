"""Module defining the database models."""

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Section(Base):
    """Model of the `sections` table."""

    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    order = Column(Integer, nullable=False, unique=True, index=True)
    html_id = Column(String, nullable=False, unique=True, index=True)
    has_page = Column(Boolean, nullable=False)
