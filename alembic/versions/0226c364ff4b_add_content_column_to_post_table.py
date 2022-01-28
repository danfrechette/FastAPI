"""Add Content Column to post Table

Revision ID: 0226c364ff4b
Revises: fa50fed410a2
Create Date: 2022-01-27 08:57:50.762617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0226c364ff4b'
down_revision = 'fa50fed410a2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass