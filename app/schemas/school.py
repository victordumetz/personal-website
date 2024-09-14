"""Submodule defining the school schema."""

from pydantic import BaseModel, ConfigDict


class SchoolBase(BaseModel):
    """Base schema for a school."""

    name: str
    location: str


class SchoolCreate(SchoolBase):
    """Create schema for a school."""


class School(SchoolBase):
    """School schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
