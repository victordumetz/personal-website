"""Submodule defining the language related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.language as model
import app.schemas.language as schema

CEFR_LEVELS = {
    1: "A1",
    2: "A2",
    3: "B1",
    4: "B2",
    5: "C1",
    6: "C2",
    7: "Native",
}


def get_language(db: Session, language_id: int) -> model.Language:
    """Get a language by ID."""
    return (
        db.query(model.Language)
        .filter(model.Language.id == language_id)
        .first()
    )


def get_languages(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.Language]:
    """Get all languages."""
    return db.query(model.Language).offset(skip).limit(limit).all()


def create_language(
    db: Session, language: schema.LanguageCreate
) -> model.Language:
    """Create a language."""
    cefr_level = CEFR_LEVELS[language.level]
    db_language = model.Language(
        name=language.name,
        level=language.level,
        cefr_level=cefr_level,
    )
    db.add(db_language)
    db.commit()
    db.refresh(db_language)

    return db_language
