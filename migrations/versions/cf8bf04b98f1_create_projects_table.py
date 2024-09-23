"""Create `projects` table.

Revision ID: cf8bf04b98f1
Revises: ef939f1abe35
Create Date: 2024-09-17 18:18:15.392327
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cf8bf04b98f1"
down_revision: str | None = "ef939f1abe35"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

SEED_PROJECTS = [
    {
        "name": "This website",
        "description": (
            "My personal website, built with a minimal setup using HTMX and "
            "FastAPI."
        ),
        "order": 1,
        "github_url": "https://github.com/victordumetz/personal-website",
        "image_path": "personal-website.png",
    },
]


def upgrade() -> None:
    """Create the `projects` table."""
    projects_table = op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column("github_url", sa.String(), nullable=True),
        sa.Column("image_path", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("github_url"),
    )
    op.create_index(op.f("ix_projects_id"), "projects", ["id"], unique=False)
    op.create_index(
        op.f("ix_projects_name"), "projects", ["name"], unique=True
    )
    op.create_index(
        op.f("ix_projects_order"), "projects", ["order"], unique=True
    )

    op.bulk_insert(projects_table, SEED_PROJECTS)


def downgrade() -> None:
    """Drop the `projects` table."""
    op.drop_index(op.f("ix_projects_order"), table_name="projects")
    op.drop_index(op.f("ix_projects_name"), table_name="projects")
    op.drop_index(op.f("ix_projects_id"), table_name="projects")
    op.drop_table("projects")
