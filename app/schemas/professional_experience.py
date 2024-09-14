"""Submodule defining the professional experience schema."""

from datetime import date

from pydantic import BaseModel, ConfigDict


class ProfessionalExperienceBase(BaseModel):
    """Base schema for a professional experience."""

    job_title: str
    date_from: date
    date_to: date
    company_id: int


class ProfessionalExperienceCreate(ProfessionalExperienceBase):
    """Create schema for a professional experience."""


class ProfessionalExperience(ProfessionalExperienceBase):
    """Professional experience schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
