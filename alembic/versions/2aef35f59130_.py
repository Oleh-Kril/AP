"""empty message

Revision ID: 2aef35f59130
Revises: e14ca240c37b
Create Date: 2022-11-21 13:26:58.513681

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2aef35f59130'
down_revision = 'e14ca240c37b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('password_hash', sa.String(length=260), nullable=False))
    op.drop_column('admin', 'token')
    op.add_column('user', sa.Column('password_hash', sa.String(length=260), nullable=False))
    op.drop_column('user', 'token')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', mysql.VARCHAR(length=260), nullable=False))
    op.drop_column('user', 'password_hash')
    op.add_column('admin', sa.Column('token', mysql.VARCHAR(length=260), nullable=False))
    op.drop_column('admin', 'password_hash')
    # ### end Alembic commands ###
