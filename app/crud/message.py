"""Submodule defining the message related CRUD functions."""

from sqlalchemy.orm import Session

import app.models.message as model
import app.schemas.message as schema


def get_message(db: Session, message_id: int) -> model.Message:
    """Get a message by ID."""
    return (
        db.query(model.Message).filter(model.Message.id == message_id).first()
    )


def get_messages(
    db: Session, skip: int = 0, limit: int = 100
) -> list[model.Message]:
    """Get all messages."""
    return db.query(model.Message).offset(skip).limit(limit).all()


def create_message(
    db: Session, message: schema.MessageCreate
) -> model.Message:
    """Create a message."""
    db_message = model.Message(
        name=message.name,
        email=message.email,
        message=message.message,
        sent_datetime=message.sent_datetime,
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message
