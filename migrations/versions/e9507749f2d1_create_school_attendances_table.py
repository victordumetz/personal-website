"""Create `school_attendances` table.

Revision ID: e9507749f2d1
Revises: 2e7bfed0e4f8
Create Date: 2024-09-14 15:48:55.109549
"""

from collections.abc import Sequence
from datetime import date

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e9507749f2d1"
down_revision: str | None = "2e7bfed0e4f8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

SEED_SCHOOL_ATTENDANCES = [
    {
        "content": ("MSc. in Data Analytics and Artificial Intelligence"),
        "date_from": date(2019, 9, 1),
        "date_to": date(2020, 8, 1),
        "school_id": 1,
    },
    {
        "content": ("Master's in Business Management"),
        "date_from": date(2016, 9, 1),
        "date_to": date(2019, 8, 1),
        "school_id": 1,
    },
    {
        "content": "Preparatory School in Mathematics and Physics",
        "date_from": date(2014, 9, 1),
        "date_to": date(2016, 8, 1),
        "school_id": 2,
    },
]


def upgrade() -> None:
    """Create the `school_attendances` table."""
    school_attendances_table = op.create_table(
        "school_attendances",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("date_from", sa.Date(), nullable=False),
        sa.Column("date_to", sa.Date(), nullable=False),
        sa.Column("school_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["school_id"], ["schools.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content"),
    )
    op.create_index(
        op.f("ix_school_attendances_date_from"),
        "school_attendances",
        ["date_from"],
        unique=False,
    )
    op.create_index(
        op.f("ix_school_attendances_date_to"),
        "school_attendances",
        ["date_to"],
        unique=False,
    )
    op.create_index(
        op.f("ix_school_attendances_id"),
        "school_attendances",
        ["id"],
        unique=False,
    )

    op.bulk_insert(school_attendances_table, SEED_SCHOOL_ATTENDANCES)


def downgrade() -> None:
    """Drop the `school_attendances` table."""
    op.drop_index(
        op.f("ix_school_attendances_id"), table_name="school_attendances"
    )
    op.drop_index(
        op.f("ix_school_attendances_date_to"), table_name="school_attendances"
    )
    op.drop_index(
        op.f("ix_school_attendances_date_from"),
        table_name="school_attendances",
    )
    op.drop_table("school_attendances")
