"""empty message

Revision ID: 81ba2ba97a86
Revises: 
Create Date: 2022-10-27 14:12:28.272301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81ba2ba97a86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=25), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('token', sa.String(length=260), nullable=False),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('admin_id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('country',
    sa.Column('country_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('country_id'),
    sa.UniqueConstraint('country_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('director',
    sa.Column('director_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('director_id'),
    sa.UniqueConstraint('director_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('genre',
    sa.Column('genre_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('genre_id'),
    sa.UniqueConstraint('genre_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('language',
    sa.Column('language_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('language_id'),
    sa.UniqueConstraint('language_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=25), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('token', sa.String(length=260), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('movie',
    sa.Column('movie_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('poster_url', sa.String(length=400), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('created_year', sa.DATE(), nullable=False),
    sa.Column('long', sa.Integer(), nullable=False),
    sa.Column('age_restriction', sa.Integer(), nullable=False),
    sa.Column('trailer_url', sa.String(length=150), nullable=True),
    sa.Column('id_country', sa.Integer(), nullable=False),
    sa.Column('id_genre', sa.Integer(), nullable=False),
    sa.Column('id_director', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_country'], ['country.country_id'], ),
    sa.ForeignKeyConstraint(['id_director'], ['director.director_id'], ),
    sa.ForeignKeyConstraint(['id_genre'], ['genre.genre_id'], ),
    sa.PrimaryKeyConstraint('movie_id'),
    sa.UniqueConstraint('movie_id')
    )
    op.create_table('scheduled_movie',
    sa.Column('scheduled_movie_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_time', sa.DATETIME(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('hall', sa.String(length=3), nullable=False),
    sa.Column('type', sa.Enum('2D', '3D', '4D'), nullable=True),
    sa.Column('id_language', sa.Integer(), nullable=False),
    sa.Column('id_movie', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_language'], ['language.language_id'], ),
    sa.ForeignKeyConstraint(['id_movie'], ['movie.movie_id'], ),
    sa.PrimaryKeyConstraint('scheduled_movie_id'),
    sa.UniqueConstraint('scheduled_movie_id')
    )
    op.create_table('ticket',
    sa.Column('ticket_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('row_n', sa.Integer(), nullable=False),
    sa.Column('seat_n', sa.Integer(), nullable=False),
    sa.Column('id_language', sa.Integer(), nullable=False),
    sa.Column('id_scheduled_movie', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_language'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['id_scheduled_movie'], ['scheduled_movie.scheduled_movie_id'], ),
    sa.PrimaryKeyConstraint('ticket_id'),
    sa.UniqueConstraint('ticket_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    op.drop_table('scheduled_movie')
    op.drop_table('movie')
    op.drop_table('user')
    op.drop_table('language')
    op.drop_table('genre')
    op.drop_table('director')
    op.drop_table('country')
    op.drop_table('admin')
    # ### end Alembic commands ###
