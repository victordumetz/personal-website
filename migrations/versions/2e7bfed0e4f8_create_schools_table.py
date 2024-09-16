"""Create `schools` table.

Revision ID: 2e7bfed0e4f8
Revises: 7a1e597ee27c
Create Date: 2024-09-14 15:33:16.108901
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2e7bfed0e4f8"
down_revision: str | None = "7a1e597ee27c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


SEED_SCHOOLS = [
    {"name": "EDHEC Business School", "location": "Lille, France"},
    {"name": "Lycée Faidherbe", "location": "Lille, France"},
]


def upgrade() -> None:
    """Create the `schools` table."""
    schools_table = op.create_table(
        "schools",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_schools_id"), "schools", ["id"], unique=False)
    op.create_index(op.f("ix_schools_name"), "schools", ["name"], unique=True)

    op.bulk_insert(schools_table, SEED_SCHOOLS)


def downgrade() -> None:
    """Drop the `schools` table."""
    op.drop_index(op.f("ix_schools_name"), table_name="schools")
    op.drop_index(op.f("ix_schools_id"), table_name="schools")
    op.drop_table("schools")
