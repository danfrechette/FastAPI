"""Create Posts Table

Revision ID: fa50fed410a2
Revises: 
Create Date: 2022-01-27 08:54:58.651298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa50fed410a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
