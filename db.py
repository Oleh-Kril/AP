from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

engine = create_engine('mysql+pymysql://root:Klym305@localhost:3306/pp_db1')
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column('user_id', Integer, primary_key=True, nullable=False, unique=True,
                     autoincrement=True)
    user_name = Column('user_name', String(25), nullable=False, unique=True)
    full_name = Column('first_name', String(30), nullable=False)
    token = Column('token', String(260), nullable=False)
    email = Column('email', String(45), nullable=False, unique=True)
    phone = Column('phone', String(13), nullable=False)


class Language(Base):
    __tablename__ = 'language'

    language_id = Column('language_id', Integer, primary_key=True, nullable=False, unique=True,
                         autoincrement=True)
    name = Column('name', String(20), nullable=False, unique=True)


class Country(Base):
    __tablename__ = 'country'

    country_id = Column('country_id', Integer, primary_key=True, nullable=False, unique=True,
                        autoincrement=True)
    name = Column('name', String(20), nullable=False, unique=True)


class Genre(Base):
    __tablename__ = 'genre'

    genre_id = Column('genre_id', Integer, primary_key=True, nullable=False, unique=True,
                      autoincrement=True)
    name = Column('name', String(20), nullable=False, unique=True)


class Director(Base):
    __tablename__ = 'director'

    director_id = Column('director_id', Integer, primary_key=True, nullable=False, unique=True,
                         autoincrement=True)
    name = Column('name', String(30), nullable=False, unique=True)


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column('admin_id', Integer, primary_key=True, nullable=False, unique=True,
                      autoincrement=True)
    user_name = Column('user_name', String(25), nullable=False, unique=True)
    full_name = Column('first_name', String(30), nullable=False)
    token = Column('token', String(260), nullable=False)


class Movie(Base):
    __tablename__ = "movie"

    movie_id = Column('movie_id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column('title', String(40), nullable=False)
    poster_url = Column('poster_url', String(400), nullable=False)
    description = Column('description', String(150))
    created_year = Column('created_year', DATE, nullable=False)
    long = Column('long', Integer, nullable=False)
    age_restriction = Column('age_restriction', Integer, nullable=False)
    trailer_url = Column('trailer_url', String(150))
    id_country = Column('id_country', Integer,  ForeignKey(Country.country_id),  nullable=False)
    id_genre = Column('id_genre', Integer, ForeignKey(Genre.genre_id),  nullable=False)
    id_director = Column('id_director', Integer, ForeignKey(Director.director_id),  nullable=False)

    country = relationship(Country, backref='advertisement', lazy='joined')
    genre = relationship(Genre, backref='advertisement', lazy='joined')
    director = relationship(Director, backref='advertisement', lazy='joined')


class ScheduledMovie(Base):
    __tablename__ = "scheduled_movie"

    scheduled_movie_id = Column('scheduled_movie_id', Integer, primary_key=True, nullable=False, unique=True,
                                autoincrement=True)
    date_time = Column('date_time', DATETIME, nullable=False)
    price = Column('price', Integer, nullable=False)
    hall = Column('hall', String(3), nullable=False)
    type = Column('type', Enum("2D", "3D", "4D"))
    id_language = Column('id_language', Integer, ForeignKey(Language.language_id), nullable=False)
    id_movie = Column('id_movie', Integer, ForeignKey(Movie.movie_id), nullable=False)

    language = relationship(Language, backref='advertisement', lazy='joined')
    movie = relationship(Movie, backref='advertisement', lazy='joined')


class Ticket(Base):
    __tablename__ = "ticket"

    ticket_id = Column('ticket_id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    row_n = Column('row_n', Integer, nullable=False)
    seat_n = Column('seat_n', Integer, nullable=False)
    id_user = Column('id_language', Integer, ForeignKey(User.user_id), nullable=False)
    id_scheduled_movie = Column('id_scheduled_movie', Integer, ForeignKey(ScheduledMovie.scheduled_movie_id),
                                nullable=False)

    user = relationship(User, backref='advertisement', lazy='joined')
    scheduled_movie = relationship(ScheduledMovie, backref='advertisement', lazy='joined')

