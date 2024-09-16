"""Submodule defining the pro. responsibility related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.professional_responsibility as model
import app.schemas.professional_responsibility as schema


def get_professional_responsibility(
    db: Session, professional_responsibility_id: int
) -> model.ProfessionalResponsibility:
    """Get a professional_responsibility by ID."""
    return (
        db.query(model.ProfessionalResponsibility)
        .filter(
            model.ProfessionalResponsibility.id
            == professional_responsibility_id
        )
        .first()
    )


def get_professional_responsibilities(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.ProfessionalResponsibility]:
    """Get all professional responsibilities."""
    return (
        db.query(model.ProfessionalResponsibility)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_professional_responsibility(
    db: Session,
    professional_responsibility: schema.ProfessionalResponsibilityCreate,
) -> model.ProfessionalResponsibility:
    """Create a professional responsibility."""
    db_professional_responsibility = model.ProfessionalResponsibility(
        description=professional_responsibility.description,
        order=professional_responsibility.order,
        professional_experience_id=professional_responsibility.professional_experience_id,
    )
    db.add(db_professional_responsibility)
    db.commit()
    db.refresh(db_professional_responsibility)

    return db_professional_responsibility
