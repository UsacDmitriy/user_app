"""Set user name not nullable without autogenerate

Revision ID: 101da3b7cac4
Revises: d436e5eae955
Create Date: 2022-10-28 16:10:53.815647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '101da3b7cac4'
down_revision = 'd436e5eae955'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("user", "username", nullable=False)
    op.alter_column("user", "short_description", nullable=False)


def downgrade() -> None:
    op.alter_column("user", "username", nullable=True)
    op.alter_column("user", "short_description", nullable=True)
