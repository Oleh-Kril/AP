"""empty message

Revision ID: 25db4e6b19ec
Revises: add5add9cce8
Create Date: 2022-11-03 12:19:07.019972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25db4e6b19ec'
down_revision = 'add5add9cce8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('country', table_name='movie')
    op.drop_index('director', table_name='movie')
    op.drop_index('genre', table_name='movie')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('genre', 'movie', ['genre'], unique=False)
    op.create_index('director', 'movie', ['director'], unique=False)
    op.create_index('country', 'movie', ['country'], unique=False)
    # ### end Alembic commands ###
