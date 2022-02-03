"""auto-vote

Revision ID: 51ca565305cc
Revises: 5b8f3c833a31
Create Date: 2022-01-27 11:41:52.624045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '51ca565305cc'
down_revision = '5b8f3c833a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='True', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.drop_column('posts', 'publish')
    op.drop_column('posts', 'create_at')
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.drop_column('users', 'create_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('create_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("'2022-01-27 09:25:27.056515-05'::timestamp with time zone"), autoincrement=False, nullable=False))
    op.drop_column('users', 'created_at')
    op.add_column('posts', sa.Column('create_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.add_column('posts', sa.Column('publish', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False))
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    op.drop_table('votes')
    # ### end Alembic commands ###