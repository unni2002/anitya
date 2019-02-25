"""Add version pattern

Revision ID: 708f6f26b4b6
Revises: 1ab95561edae
Create Date: 2019-04-25 16:51:03.302314
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "708f6f26b4b6"
down_revision = "1ab95561edae"


def upgrade():
    """ Add version_pattern to projects table. """
    op.add_column(
        "projects", sa.Column("version_pattern", sa.String(200), nullable=True)
    )


def downgrade():
    """ Remove version_pattern from project table. """
    op.drop_column("projects", "version_pattern")