"""add content column to posts table

Revision ID: 8e3f21dd395a
Revises: e830a39ce85b
Create Date: 2026-07-27 10:00:45.491132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e3f21dd395a'
down_revision: Union[str, Sequence[str], None] = 'e830a39ce85b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
