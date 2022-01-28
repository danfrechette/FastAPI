"""Add User Table

Revision ID: ebffba755ad4
Revises: 0226c364ff4b
Create Date: 2022-01-27 09:02:07.966179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebffba755ad4'
down_revision = '0226c364ff4b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(),nullable=False),
        sa.Column('email', sa.String(),nullable=False),
        sa.Column('password', sa.String(),nullable=False),
        sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users') 
    pass
