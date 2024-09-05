"""Create the `sections` table.

Revision ID: d4e6104fbced
Revises:
Create Date: 2024-09-05 13:17:41.955008

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d4e6104fbced"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Create the `sections`table."""
    sections = op.create_table(
        "sections",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False, unique=True, index=True),
        sa.Column(
            "order", sa.Integer, nullable=False, unique=True, index=True
        ),
        sa.Column(
            "html_id", sa.String, nullable=False, unique=True, index=True
        ),
        sa.Column("has_page", sa.Boolean, nullable=False),
    )

    op.bulk_insert(
        sections,
        [
            {
                "name": "About",
                "order": 1,
                "html_id": "about",
                "has_page": False,
            },
            {
                "name": "Skills",
                "order": 2,
                "html_id": "skills",
                "has_page": False,
            },
            {
                "name": "Projects",
                "order": 3,
                "html_id": "projects",
                "has_page": True,
            },
            {
                "name": "Contact",
                "order": 4,
                "html_id": "contact",
                "has_page": False,
            },
        ],
    )


def downgrade() -> None:
    """Drop the `sections` table."""
    op.drop_table("sections")
