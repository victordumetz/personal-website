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


class FormattedProfessionalExperience(BaseModel):
    """Formatted professional experience schema.

    The formatted experiences include the company information as well as
    the responsibility descriptions.
    """

    model_config = ConfigDict(from_attributes=True)

    company_name: str
    location: str
    job_title: str
    year_month_from: str
    year_month_to: str
    responsibilities: list[str]
