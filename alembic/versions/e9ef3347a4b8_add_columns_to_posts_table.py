"""add columns to posts table

Revision ID: e9ef3347a4b8
Revises: 00edf99a91b1
Create Date: 2026-07-28 13:18:33.706419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = 'e9ef3347a4b8'
down_revision: Union[str, Sequence[str], None] = '00edf99a91b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default=sa.text("false")))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
    pass
