"""Module defining the data schemas."""

from pydantic import BaseModel, ConfigDict


class SectionBase(BaseModel):
    """Base schema of a section."""

    name: str
    order: int
    has_page: bool


class SectionCreate(SectionBase):
    """Create schema of a section."""


class Section(SectionBase):
    """Schema of a section."""

    model_config = ConfigDict(from_attributes=True)

    id: int
