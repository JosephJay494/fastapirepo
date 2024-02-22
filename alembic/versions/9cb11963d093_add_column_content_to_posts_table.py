"""add column content to posts table

Revision ID: 9cb11963d093
Revises: 5616db7e6924
Create Date: 2024-02-21 16:26:10.967843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cb11963d093'
down_revision: Union[str, None] = '5616db7e6924'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
