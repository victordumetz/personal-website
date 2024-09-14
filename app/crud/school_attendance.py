"""Submodule defining the school attendance related CRUD functions."""

from sqlalchemy.orm import Session

import app.schemas.school_attendance as schema
from app.models.school_attendance import SchoolAttendance


def get_school_attendance(
    db: Session, school_attendance_id: int
) -> SchoolAttendance:
    """Get a school_attendance by ID."""
    return (
        db.query(SchoolAttendance)
        .filter(SchoolAttendance.id == school_attendance_id)
        .first()
    )


def get_school_attendances(
    db: Session, skip: int = 0, limit: int = 100
) -> list[SchoolAttendance]:
    """Get all school attendances."""
    return db.query(SchoolAttendance).offset(skip).limit(limit).all()


def create_school_attendance(
    db: Session, school_attendance: schema.SchoolAttendanceCreate
) -> SchoolAttendance:
    """Create a school attendance."""
    db_school_attendance = SchoolAttendance(
        content=school_attendance.content,
        date_from=school_attendance.date_from,
        date_to=school_attendance.date_to,
        school_id=school_attendance.school_id,
    )
    db.add(db_school_attendance)
    db.commit()
    db.refresh(db_school_attendance)

    return db_school_attendance
