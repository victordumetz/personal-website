"""Submodule defining the language schema."""

from typing import Literal

from pydantic import BaseModel, ConfigDict


class LanguageBase(BaseModel):
    """Base schema for a language."""

    name: str
    level: int
    cefr_level: Literal["Native", "C2", "C1", "B2", "B1", "A2", "A1"]


class LanguageCreate(LanguageBase):
    """Create schema for a language."""


class Language(LanguageBase):
    """Language schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
