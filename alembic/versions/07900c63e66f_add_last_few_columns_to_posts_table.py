"""add last few columns to posts table

Revision ID: 07900c63e66f
Revises: 88a2ad1510e5
Create Date: 2024-02-22 04:02:21.844341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07900c63e66f'
down_revision: Union[str, None] = '88a2ad1510e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', 
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
                            ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
