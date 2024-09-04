"""Module defining the CRUD functions."""

from sqlalchemy.orm import Session

from . import models, schemas


def create_section(
    db: Session, section: schemas.SectionCreate
) -> models.Section:
    """Create a section in the database."""
    html_id = section.name.lower().replace(" ", "-")

    db_section = models.Section(
        name=section.name,
        order=section.order,
        html_id=html_id,
        has_page=section.has_page,
    )

    db.add(db_section)
    db.commit()
    db.refresh(db_section)

    return db_section


def get_sections(db: Session) -> list[models.Section]:
    """Return all sections from the database.

    The sections are ordered by `order`.
    """
    return db.query(models.Section).order_by(models.Section.order).all()
