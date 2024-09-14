"""Create `professional_responsibilities` table.

Revision ID: 7a1e597ee27c
Revises: 3ab290d3dde7
Create Date: 2024-09-14 11:54:32.690876
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7a1e597ee27c"
down_revision: str | None = "3ab290d3dde7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

SEED_PROFESSIONAL_RESPONSIBILITIES = [
    {
        "description": (
            "Development of complex KPIs and automation of their "
            "computations (using Airflow)."
        ),
        "order": 1,
        "professional_experience_id": 1,
    },
    {
        "description": (
            "Development of a deep-autoencoding clustering algorithm "
            "(using Tensorflow)."
        ),
        "order": 2,
        "professional_experience_id": 1,
    },
    {
        "description": (
            "Analysis of voucher effectiveness using propensity "
            "score matching, taking into account the non-random "
            "nature of voucher distribution."
        ),
        "order": 3,
        "professional_experience_id": 1,
    },
    {
        "description": (
            "Redesign of a complete ETL pipeline for data quality and "
            "monitoring."
        ),
        "order": 4,
        "professional_experience_id": 1,
    },
    {
        "description": (
            "Creation of complex SQL queries, optimisation of already "
            "deployed queries, training of database users on best "
            "practices and advanced SQL in a company-wide SQL "
            "training program."
        ),
        "order": 5,
        "professional_experience_id": 1,
    },
    {
        "description": (
            "Accounts portfolio analysis using integer programming "
            "in order to maximise value creation from every sales "
            "representative, automation of accounts' reassignment "
            "via Python."
        ),
        "order": 1,
        "professional_experience_id": 2,
    },
    {
        "description": (
            "Creation of a new sales dashboard from the choice of "
            "meaningful KPIs, to the design of its data-structure, "
            "to the deployment of it all over Europe (approx. 15 "
            "countries and 250 users)."
        ),
        "order": 2,
        "professional_experience_id": 2,
    },
    {
        "description": (
            "Development of a new commission scheme for the pricing "
            "team to align the interests of the employees with the "
            "ones of the company, presentation to the CEO and during "
            "the board meeting, implementation (using R and Shiny)."
        ),
        "order": 3,
        "professional_experience_id": 2,
    },
    {
        "description": (
            "Conduct of various analyses for C-level executives "
            "using diverse machine learning techniques."
        ),
        "order": 4,
        "professional_experience_id": 2,
    },
    {
        "description": (
            "Continuation of projects initiated during my internship."
        ),
        "order": 1,
        "professional_experience_id": 3,
    },
    {
        "description": (
            "Development of a competency-based performance "
            "management program (WinDev)."
        ),
        "order": 2,
        "professional_experience_id": 3,
    },
    {
        "description": (
            "Excel spreadsheets design (using VBA) in order to "
            "provide the business managers with effective project "
            "management tools. Use of these tools to follow up on a €"
            "200k project."
        ),
        "order": 1,
        "professional_experience_id": 4,
    },
    {
        "description": (
            "Creation, networking and management of databases (SQL) "
            "and development of a strategic workforce planning "
            "application (WinDev)."
        ),
        "order": 2,
        "professional_experience_id": 4,
    },
    {
        "description": (
            "Documentation and training of the end-users to the "
            "developed tools."
        ),
        "order": 3,
        "professional_experience_id": 4,
    },
]


def upgrade() -> None:
    """Create the `personnal_responsibilities` table."""
    professional_responsibilities_table = op.create_table(
        "professional_responsibilities",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column("professional_experience_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["professional_experience_id"],
            ["professional_experiences.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("description"),
        sa.UniqueConstraint("professional_experience_id", "order"),
    )
    op.create_index(
        op.f("ix_professional_responsibilities_id"),
        "professional_responsibilities",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_professional_responsibilities_order"),
        "professional_responsibilities",
        ["order"],
        unique=False,
    )

    op.bulk_insert(
        professional_responsibilities_table,
        SEED_PROFESSIONAL_RESPONSIBILITIES,
    )


def downgrade() -> None:
    """Drop the `personnal_responsibilities` table."""
    op.drop_index(
        op.f("ix_professional_responsibilities_order"),
        table_name="professional_responsibilities",
    )
    op.drop_index(
        op.f("ix_professional_responsibilities_id"),
        table_name="professional_responsibilities",
    )
    op.drop_table("professional_responsibilities")
