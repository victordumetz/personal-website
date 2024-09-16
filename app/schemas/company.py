"""Submodule defining the company schema."""

from pydantic import BaseModel, ConfigDict


class CompanyBase(BaseModel):
    """Base schema for a company."""

    name: str
    location: str


class CompanyCreate(CompanyBase):
    """Create schema for a company."""


class Company(CompanyBase):
    """Company schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
