"""Second commit
Revision ID: 622304e2bbb1
Revises:
Create Date: 2021-11-07 22:43:11.025783
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '622304e2bbb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('body', sa.String(length=8000), nullable=True),
    sa.Column('version', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('article_id')
    )
    op.create_table('moderator',
    sa.Column('moderator_id', sa.Integer(), nullable=False),
    sa.Column('moderatorname', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('moderatorkey', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('moderator_id')
    )
    op.create_table('state',
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('state_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('updated_article',
    sa.Column('updated_article_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('moderator_id', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('article_body', sa.String(length=8000), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.article_id'], ),
    sa.ForeignKeyConstraint(['moderator_id'], ['moderator.moderator_id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['state.state_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('updated_article_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('updated_article')
    op.drop_table('user')
    op.drop_table('state')
    op.drop_table('moderator')
    op.drop_table('article')
    # ### end Alembic commands ###