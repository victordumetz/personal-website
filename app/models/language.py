"""Submodule defining the language model."""

from sqlalchemy import Column, Integer, String

from app.database import Base


class Language(Base):
    """Model defining a language in the database."""

    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    level = Column(Integer, nullable=False, index=True)
    cefr_level = Column(String, nullable=False)
