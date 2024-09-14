"""Submodule defining the school related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.school as model
import app.schemas.school as schema


def get_school(db: Session, school_id: int) -> model.School:
    """Get a school by ID."""
    return db.query(model.School).filter(model.School.id == school_id).first()


def get_schools(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.School]:
    """Get all schools."""
    return db.query(model.School).offset(skip).limit(limit).all()


def create_school(db: Session, school: schema.SchoolCreate) -> model.School:
    """Create a school."""
    db_school = model.School(name=school.name, location=school.location)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)

    return db_school
