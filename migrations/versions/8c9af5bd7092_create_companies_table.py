"""Create `companies` table.

Revision ID: 8c9af5bd7092
Revises:
Create Date: 2024-09-11 16:18:19.139659
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8c9af5bd7092"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None
SEED_COMPANIES = [
    {
        "name": "AUTO1 Group",
        "location": "Berlin, Germany",
    },
    {
        "name": "INDUSTEAM Group",
        "location": "Leulinghem, France",
    },
]


def upgrade() -> None:
    """Create the `companies` table."""
    companies_table = op.create_table(
        "companies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_companies_id"), "companies", ["id"], unique=False)
    op.create_index(
        op.f("ix_companies_name"), "companies", ["name"], unique=True
    )

    op.bulk_insert(
        companies_table,
        SEED_COMPANIES,
    )


def downgrade() -> None:
    """Drop the `companies` table."""
    op.drop_index(op.f("ix_companies_name"), table_name="companies")
    op.drop_index(op.f("ix_companies_id"), table_name="companies")
    op.drop_table("companies")
