"""add user table

Revision ID: 0f7f85ca21ae
Revises: 8e3f21dd395a
Create Date: 2026-07-27 10:41:31.419024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f7f85ca21ae'
down_revision: Union[str, Sequence[str], None] = '8e3f21dd395a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False, unique=True), 
                    sa.Column('password', sa.String(), nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
