"""Create `messages` table.

Revision ID: 92c213e57615
Revises: cf8bf04b98f1
Create Date: 2024-09-24 12:46:51.687934
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "92c213e57615"
down_revision: str | None = "cf8bf04b98f1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Create the `messages` table."""
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("sent_datetime", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_messages_email"), "messages", ["email"], unique=False
    )
    op.create_index(op.f("ix_messages_id"), "messages", ["id"], unique=False)
    op.create_index(
        op.f("ix_messages_name"), "messages", ["name"], unique=False
    )
    op.create_index(
        op.f("ix_messages_sent_datetime"),
        "messages",
        ["sent_datetime"],
        unique=False,
    )


def downgrade() -> None:
    """Drop the `messages` table."""
    op.drop_index(op.f("ix_messages_sent_datetime"), table_name="messages")
    op.drop_index(op.f("ix_messages_name"), table_name="messages")
    op.drop_index(op.f("ix_messages_id"), table_name="messages")
    op.drop_index(op.f("ix_messages_email"), table_name="messages")
    op.drop_table("messages")
