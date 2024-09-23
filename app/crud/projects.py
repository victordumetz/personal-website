"""Submodule defining the project related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.project as model
import app.schemas.project as schema


def get_project(db: Session, project_id: int) -> model.Project:
    """Get a project by ID."""
    return (
        db.query(model.Project).filter(model.Project.id == project_id).first()
    )


def get_projects(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.Project]:
    """Get all projects."""
    return (
        db.query(model.Project)
        .order_by(model.Project.order)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_project(
    db: Session, project: schema.ProjectCreate
) -> model.Project:
    """Create a project."""
    db_project = model.Project(
        name=project.name,
        description=project.description,
        order=project.order,
        github_url=project.github_url,
        image_path=project.image_path,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project
