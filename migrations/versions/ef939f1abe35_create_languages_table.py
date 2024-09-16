"""Create `languages` table.

Revision ID: ef939f1abe35
Revises: e9507749f2d1
Create Date: 2024-09-14 17:09:29.804479
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ef939f1abe35"
down_revision: str | None = "e9507749f2d1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

SEED_LANGUAGES = [
    {"name": "French", "level": 7, "cefr_level": "Native"},
    {"name": "English", "level": 6, "cefr_level": "C2"},
    {"name": "German", "level": 5, "cefr_level": "C1"},
    {"name": "Japanese", "level": 3, "cefr_level": "B1"},
    {"name": "Spanish", "level": 3, "cefr_level": "B1"},
    {"name": "Vietnamese", "level": 1, "cefr_level": "A1"},
]


def upgrade() -> None:
    """Create the `languages` table."""
    languages_table = op.create_table(
        "languages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("cefr_level", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_languages_id"), "languages", ["id"], unique=False)
    op.create_index(
        op.f("ix_languages_level"), "languages", ["level"], unique=False
    )
    op.create_index(
        op.f("ix_languages_name"), "languages", ["name"], unique=True
    )

    op.bulk_insert(languages_table, SEED_LANGUAGES)


def downgrade() -> None:
    """Drop the `languages` table."""
    op.drop_index(op.f("ix_languages_name"), table_name="languages")
    op.drop_index(op.f("ix_languages_level"), table_name="languages")
    op.drop_index(op.f("ix_languages_id"), table_name="languages")
    op.drop_table("languages")
