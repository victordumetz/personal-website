"""Submodule defining the message model."""

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class Message(Base):
    """Model defining a message in the database."""

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    message = Column(Text, nullable=False)
    sent_datetime = Column(DateTime, nullable=False, index=True)
