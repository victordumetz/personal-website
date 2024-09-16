"""Submodule defining the professional responsibility schema."""

from pydantic import BaseModel, ConfigDict


class ProfessionalResponsibilityBase(BaseModel):
    """Base schema for a professional responsibility."""

    description: str
    order: int
    professional_experience_id: int


class ProfessionalResponsibilityCreate(ProfessionalResponsibilityBase):
    """Create schema for a professional responsibility."""


class ProfessionalResponsibility(ProfessionalResponsibilityBase):
    """Professional responsibility schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
