"""Submodule defining the pro. experience related CRUD functions."""

from collections.abc import Sequence

from sqlalchemy import RowMapping, desc, func, select
from sqlalchemy.orm import Session

import app.schemas.professional_experience as schema
from app.models.company import Company
from app.models.professional_experience import ProfessionalExperience
from app.models.professional_responsibility import ProfessionalResponsibility


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


def get_formatted_professional_experiences(
    db: Session,
) -> Sequence[RowMapping]:
    """Get all the formatted professional experiences."""
    return (
        db.execute(
            select(
                Company.name,
                Company.location,
                ProfessionalExperience.job_title,
                ProfessionalExperience.date_from,
                ProfessionalExperience.date_to,
                func.json_group_array(
                    ProfessionalResponsibility.description
                ).label("responsibilities"),
            )
            .join_from(Company, ProfessionalExperience)
            .join(ProfessionalResponsibility)
            .order_by(desc(ProfessionalExperience.date_from))
            .group_by(
                Company.name,
                ProfessionalExperience.job_title,
                ProfessionalExperience.date_from,
            )
        )
        .mappings()
        .all()
    )
