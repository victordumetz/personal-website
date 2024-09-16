"""Create `professional_experiences` table.

Revision ID: 3ab290d3dde7
Revises: 8c9af5bd7092
Create Date: 2024-09-11 17:36:25.231614
"""

from collections.abc import Sequence
from datetime import date

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3ab290d3dde7"
down_revision: str | None = "8c9af5bd7092"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

SEED_PROFESSIONAL_EXPERIENCES = [
    {
        "job_title": "Data Scientist",
        "date_from": date(2020, 10, 1),
        "date_to": date(2022, 5, 1),
        "company_id": 1,
    },
    {
        "job_title": "Business Analytics Intern",
        "date_from": date(2018, 11, 1),
        "date_to": date(2019, 8, 1),
        "company_id": 1,
    },
    {
        "job_title": "Temporary Worker",
        "date_from": date(2017, 8, 1),
        "date_to": date(2018, 10, 1),
        "company_id": 2,
    },
    {
        "job_title": ("Business Intelligence & Project Management Intern"),
        "date_from": date(2017, 5, 1),
        "date_to": date(2017, 8, 1),
        "company_id": 2,
    },
]


def upgrade() -> None:
    """Create the `professional_experiences` table."""
    professional_experiences_table = op.create_table(
        "professional_experiences",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("job_title", sa.String(), nullable=False),
        sa.Column("date_from", sa.Date(), nullable=False),
        sa.Column("date_to", sa.Date(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["company_id"], ["companies.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_professional_experiences_date_from"),
        "professional_experiences",
        ["date_from"],
        unique=False,
    )
    op.create_index(
        op.f("ix_professional_experiences_date_to"),
        "professional_experiences",
        ["date_to"],
        unique=False,
    )
    op.create_index(
        op.f("ix_professional_experiences_id"),
        "professional_experiences",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_professional_experiences_job_title"),
        "professional_experiences",
        ["job_title"],
        unique=True,
    )

    op.bulk_insert(
        professional_experiences_table,
        SEED_PROFESSIONAL_EXPERIENCES,
    )


def downgrade() -> None:
    """Drop the `professional_experiences` table."""
    op.drop_index(
        op.f("ix_professional_experiences_job_title"),
        table_name="professional_experiences",
    )
    op.drop_index(
        op.f("ix_professional_experiences_id"),
        table_name="professional_experiences",
    )
    op.drop_index(
        op.f("ix_professional_experiences_date_to"),
        table_name="professional_experiences",
    )
    op.drop_index(
        op.f("ix_professional_experiences_date_from"),
        table_name="professional_experiences",
    )
    op.drop_table("professional_experiences")
