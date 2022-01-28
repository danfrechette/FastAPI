"""add freign key to posts table

Revision ID: a66e95635bfc
Revises: ebffba755ad4
Create Date: 2022-01-27 09:29:16.589821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a66e95635bfc'
down_revision = 'ebffba755ad4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=-False))
    op.create_foreign_key('post_users_fk', source_table = "posts", referent_table = "users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass

