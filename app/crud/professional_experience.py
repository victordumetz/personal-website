"""Submodule defining the pro. experience related CRUD functions."""

from sqlalchemy.orm import Session

import app.schemas.professional_experience as schema


def get_professional_experience(
    db: Session, professional_experience_id: int
) -> ProfessionalExperience:
    """Get a professional_experience by ID."""
    return (
        db.query(ProfessionalExperience)
        .filter(ProfessionalExperience.id == professional_experience_id)
        .first()
    )


def get_professional_experiences(
    db: Session, skip: int = 0, limit: int = 100
) -> list[ProfessionalExperience]:
    """Get all professional experiences."""
    return db.query(ProfessionalExperience).offset(skip).limit(limit).all()


def create_professional_experience(
    db: Session, professional_experience: schema.ProfessionalExperienceCreate
) -> ProfessionalExperience:
    """Create a professional experience."""
    db_professional_experience = ProfessionalExperience(
        job_title=professional_experience.job_title,
        date_from=professional_experience.date_from,
        date_to=professional_experience.date_to,
        company_id=professional_experience.company_id,
    )
    db.add(db_professional_experience)
    db.commit()
    db.refresh(db_professional_experience)

    return db_professional_experience
