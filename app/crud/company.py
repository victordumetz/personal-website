"""Submodule defining the company related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.company as model
import app.schemas.company as schema


def get_company(db: Session, company_id: int) -> model.Company:
    """Get a company by ID."""
    return (
        db.query(model.Company).filter(model.Company.id == company_id).first()
    )


def get_companies(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.Company]:
    """Get all companies."""
    return db.query(model.Company).offset(skip).limit(limit).all()


def create_company(
    db: Session, company: schema.CompanyCreate
) -> model.Company:
    """Create a company."""
    db_company = model.Company(name=company.name, location=company.location)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company
