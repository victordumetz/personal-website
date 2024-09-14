"""Submodule defining the school attendance schema."""

from datetime import date

from pydantic import BaseModel, ConfigDict


class SchoolAttendanceBase(BaseModel):
    """Base schema for a school attendance."""

    content: str
    date_from: date
    date_to: date
    school_id: int


class SchoolAttendanceCreate(SchoolAttendanceBase):
    """Create schema for a school attendance."""


class SchoolAttendance(SchoolAttendanceBase):
    """School attendance schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int


class FormattedSchoolAttendance(BaseModel):
    """Formatted school attendance schema.

    The formatted attendances include information about the school.
    """

    model_config = ConfigDict(from_attributes=True)

    school_name: str
    location: str
    content: str
    year_month_from: str
    year_month_to: str
