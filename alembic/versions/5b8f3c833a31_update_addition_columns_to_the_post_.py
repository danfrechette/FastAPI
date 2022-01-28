"""update addition columns to the Post tablee

Revision ID: 5b8f3c833a31
Revises: a66e95635bfc
Create Date: 2022-01-27 10:24:51.043546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8f3c833a31'
down_revision = 'a66e95635bfc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'publish', sa.Boolean(), nullable = False, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'create_at', sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'publish')
    op.drop_column('posts', 'create_at')
    pass
