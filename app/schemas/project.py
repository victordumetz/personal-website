"""Submodule defining the project schema."""

from pydantic import BaseModel, ConfigDict, FileUrl, HttpUrl


class ProjectBase(BaseModel):
    """Base schema for a project."""

    name: str
    description: str
    order: int
    github_url: HttpUrl
    image_path: FileUrl


class ProjectCreate(ProjectBase):
    """Create schema for a project."""


class Project(ProjectBase):
    """Project schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
