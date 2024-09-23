"""Submodule defining the project model."""

from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Project(Base):
    """Model defining a project in the database."""

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    order = Column(Integer, unique=True, nullable=False, index=True)
    github_url = Column(String, unique=True)
    image_path = Column(String, nullable=False)
