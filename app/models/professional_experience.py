"""Submodule defining the professional experience model."""

from sqlalchemy import Column, Date, ForeignKey, Integer, String

from app.database import Base


class ProfessionalExperience(Base):
    """Model defining a professional experience in the database."""

    __tablename__ = "professional_experiences"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, unique=True, nullable=False, index=True)
    date_from = Column(Date, nullable=False, index=True)
    date_to = Column(Date, nullable=False, index=True)
    company_id = Column(
        Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False
    )
