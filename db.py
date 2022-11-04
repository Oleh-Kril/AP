from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from marshmallow import Schema, fields, validate, post_load, pre_load

engine = create_engine('mysql+pymysql://root:rootadmin2022@localhost:3306/cinema')
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()

class CustomBase():
    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.query(cls).all()
    @classmethod
    def post_one(cls, item):
        with Session() as session:
            session.add(item)
            session.commit()

            return 200
    @classmethod
    def get_by_id(cls, id):
        with Session() as session:
            class_id_attr = f"{cls.__name__}_id".lower()
            class_object = session.query(cls).filter(getattr(cls, class_id_attr) == id).first()
            if class_object is None:
                return 404
            return class_object


    @classmethod
    def delete_by_id(cls, id):
        with Session() as session:
            class_object = cls.get_by_id(id)

            if class_object == 404:
                return 404
            class_id_attr = f"{cls.__name__}_id".lower()
            session.query(cls).filter(getattr(cls, class_id_attr) == id).delete()
            session.commit()
            return 200

    @classmethod
    def get_with_filter(cls, parameters):
        with Session() as session:
            q = session.query(cls)
            for attr, value in parameters.items():
                q = q.filter(getattr(cls, attr).ilike(f"%%{value}%%"))

            return q.all()

    @classmethod
    def update_one(cls, id, updates):
        with Session() as session:
            if cls.get_by_id(id) == 404:
                return 404
            class_id_attr = f"{cls.__name__}_id".lower()
            session.query(cls).filter(getattr(cls, class_id_attr) == id).update(updates)
            session.commit()
            return 200
class User(CustomBase, Base):
    __tablename__ = 'user'

    user_id = Column('user_id', Integer, primary_key=True, nullable=False, unique=True,
                     autoincrement=True)
    user_name = Column('user_name', String(25), nullable=False, unique=True)
    full_name = Column('first_name', String(30), nullable=False)
    token = Column('token', String(260), nullable=False)
    email = Column('email', String(45), nullable=False, unique=True)
    phone = Column('phone', String(13), nullable=False)

    def __repr__(self):
        return f"user_id: {self.user_id}, user_name: {self.user_name}, email: {self.email}, phone: {self.phone}"

    def __init__(self, user_name, full_name, token, email, phone):
        self.user_name = user_name
        self.full_name = full_name
        self.token = token
        self.email = email
        self.phone = phone

class UserSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.String(required=True)
    full_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

    token = fields.String(load_only=True)

class Admin(CustomBase, Base):
    __tablename__ = "admin"

    admin_id = Column('admin_id', Integer, primary_key=True, nullable=False, unique=True,
                      autoincrement=True)
    user_name = Column('user_name', String(25), nullable=False, unique=True)
    full_name = Column('first_name', String(30), nullable=False)
    token = Column('token', String(260), nullable=False)

    def __init__(self, user_name, full_name, token):
        self.user_name = user_name
        self.full_name = full_name
        self.token = token

class Movie(CustomBase, Base):
    __tablename__ = "movie"

    movie_id = Column('movie_id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column('title', String(40), nullable=False)
    poster_url = Column('poster_url', String(400), nullable=False)
    description = Column('description', String(150), default=None)
    created_year = Column('created_year', DATE, nullable=False)
    long = Column('long', Integer, nullable=False)
    age_restriction = Column('age_restriction', Integer, nullable=False)
    trailer_url = Column('trailer_url', String(150), default=None)
    country = Column('country', String(50), nullable=False)
    genre = Column('genre', String(100), nullable=False)
    director =Column('director', String(60), nullable=False)

    def __init__(self, title, poster_url, created_year, long, age_restriction,
                 country, genre, director, description = "", trailer_url = ""):
        self.title = title
        self.poster_url = poster_url
        self.created_year = created_year
        self.long = long
        self.age_restriction = age_restriction
        self.genre = genre
        self.director = director
        self.country = country
        if len(description) > 0:
            self.description = description
        if len(trailer_url) > 0:
            self.trailer_url = trailer_url

    # GET
    @classmethod
    def get_preview(cls, id):
        with Session() as session:
            movie_object = session.query(cls).filter(getattr(cls, "movie_id") == id).\
                with_entities(Movie.poster_url, Movie.title, Movie.movie_id).first()
            if movie_object is None:
                return 404

            return movie_object

class MovieSchema(Schema):
    movie_id = fields.Integer()

    title = fields.String(required=True)
    poster_url = fields.Url(required=True)
    created_year = fields.Date(required=True)
    long = fields.Integer(required=True)
    age_restriction = fields.Integer(required=True)
    country = fields.String(required=True)
    genre = fields.String(required=True)
    director = fields.String(required=True)

    description = fields.String()
    trailer_url = fields.Url()

class MoviePreviewSchema(Schema):
    movie_id = fields.Integer()

    title = fields.String(required=True)
    poster_url = fields.Url(required=True)
class Hall(CustomBase, Base):
    __tablename__ = "hall"

    hall_name = Column("hall_name",String(3), primary_key=True, autoincrement=False)
    row_amount = Column("row_amount", Integer, nullable=False)
    seat_amount = Column("seat_amount", Integer, nullable=False)

    def __init__(self, hall_name, row_amount, seat_amount):
        self.hall_name = hall_name
        self.row_amount = row_amount
        self.seat_amount = seat_amount

class HallSchema(Schema):
    hall_name = fields.String()
    row_amount = fields.Integer()
    seat_amount = fields.Integer()
class ScheduledMovie(CustomBase, Base):
    __tablename__ = "scheduled_movie"

    scheduledmovie_id = Column('scheduledmovie_id', Integer, primary_key=True, nullable=False, unique=True)
    date_time = Column('date_time', DATETIME, nullable=False)
    price = Column('price', Integer, nullable=False)
    hall_name = Column('hall', String(3), ForeignKey(Hall.hall_name), nullable=False)
    type = Column('type', Enum("2D", "3D", "4D"), nullable=False)
    language = Column('language', String(40), nullable=False)
    id_movie = Column('id_movie', Integer, ForeignKey(Movie.movie_id), nullable=False)

    movie = relationship(Movie, backref='movie', lazy='joined')
    hall = relationship(Hall, backref='hall', lazy='joined')

    def __init__(self, date_time, price, hall_name, type, language, id_movie):
        self.date_time = date_time
        self.price = price
        self.type = type
        self.hall_name = hall_name
        self.language = language
        self.id_movie = id_movie

    @classmethod
    def post_one(cls, item):
        with Session() as session:
            find_movie_response = Movie.get_by_id(item.id_movie)
            if find_movie_response != 404:
                session.add(item)
                session.commit()
                return 200
            else:
                return 404
    @classmethod
    def get_with_filter(cls, parameters):
        with Session() as session:
            q = session.query(cls)
            for attr, value in parameters.items():
                if attr == "until":
                    q = q.filter(getattr(cls, "date_time") <= value)
                else:
                    q = q.filter(getattr(cls, attr).ilike(f"%%{value}%%"))

            return q.all()
    @classmethod
    def get_tickets(cls, id):
        with Session() as session:
            return session.query(Ticket).filter_by(id_scheduledmovie = id)\
                .with_entities(Ticket.row_n, Ticket.seat_n).all()

class ScheduledMovieSchema(Schema):
    scheduledmovie_id = fields.Integer()

    date_time = fields.DateTime(required=True)
    price = fields.Integer(required=True)
    type = fields.Str(validate=validate.OneOf(["2D", "3D", "4D"]), required=True)
    language = fields.String(required=True)

    hall_name = fields.String(load_only=True)
    hall = fields.Nested(HallSchema, dump_only=True)

    movie = fields.Nested(MoviePreviewSchema, dump_only=True)
    id_movie = fields.Integer(load_only=True)

class Ticket(CustomBase, Base):
    __tablename__ = "ticket"

    ticket_id = Column('ticket_id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    row_n = Column('row_n', Integer, nullable=False)
    seat_n = Column('seat_n', Integer, nullable=False)
    id_user = Column('id_user', Integer, ForeignKey(User.user_id), nullable=False)
    id_scheduledmovie = Column('id_scheduledmovie', Integer, ForeignKey(ScheduledMovie.scheduledmovie_id),
                                nullable=False)

    user = relationship(User, backref='user', lazy='joined')
    scheduled_movie = relationship(ScheduledMovie, backref='scheduled_movie', lazy='joined')


    def __init__(self, row_n, seat_n, id_user, id_scheduledmovie):
        self.row_n = row_n
        self.seat_n = seat_n
        self.id_user = id_user
        self.id_scheduledmovie = id_scheduledmovie

    @classmethod
    def get_tickets_of_user(cls, id):
        with Session() as session:
            return session.query(Ticket).filter_by(id_user = id).all()

class TicketSchema(Schema):

    ticket_id = fields.Integer()

    row_n = fields.Integer(required=True)
    seat_n = fields.Integer(required=True)

    # user = fields.Nested(UserSchema)
    id_user = fields.Integer()

    id_scheduledmovie = fields.Integer()
    scheduled_movie = fields.Nested(ScheduledMovieSchema)

if __name__ == "__main__":
    pass
    # Base.metadata.create_all(bind=engine)