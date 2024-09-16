"""Submodule defining the school attendance model."""

from sqlalchemy import Column, Date, ForeignKey, Integer, String

from app.database import Base


class SchoolAttendance(Base):
    """Model defining a school attendance in the database."""

    __tablename__ = "school_attendances"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, unique=True, nullable=False)
    date_from = Column(Date, nullable=False, index=True)
    date_to = Column(Date, nullable=False, index=True)
    school_id = Column(
        Integer, ForeignKey("schools.id", ondelete="CASCADE"), nullable=False
    )
