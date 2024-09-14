"""Submodule defining the professional responsibility model."""

from sqlalchemy import Column, ForeignKey, Integer, Text, UniqueConstraint

from app.database import Base


class ProfessionalResponsibility(Base):
    """Model defining a professional responsibility in the database."""

    __tablename__ = "professional_responsibilities"
    __table_args__ = (UniqueConstraint("professional_experience_id", "order"),)

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, unique=True, nullable=False)
    order = Column(Integer, nullable=False, index=True)
    professional_experience_id = Column(
        Integer,
        ForeignKey("professional_experiences.id", ondelete="CASCADE"),
        nullable=False,
    )
