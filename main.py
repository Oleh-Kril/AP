import json
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import Flask, jsonify, request, Response, make_response, session
from db import *
from flask_swagger_ui import get_swaggerui_blueprint


def create_app(testing: bool = True):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "ca9498317b9cd8654b62666a368e0500a8f6a1161093f19bb2edfc5642e474b8"

    def admin_token_required(func):
        # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
        @wraps(func)
        def decorated(*args, **kwargs):
            token = request.headers.get('token')
            if not token:
                return jsonify({'Alert!': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                isAdmin = data.get("admin")

                if not (isAdmin):
                    return jsonify({'Message': 'Admin access only!'}), 403

            # You can use the JWT errors in exception
            except jwt.InvalidTokenError:
                return jsonify({'Message': 'Invalid token. Please log in again.'}), 403
            except:
                return jsonify({'Message': 'Invalid token'}), 403

            return func(*args, **kwargs)

        return decorated

    def user_token_required(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            token = request.headers.get('token')
            if not token:
                return jsonify({'Alert!': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
            # You can use the JWT errors in exception
            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again.'
            except:
                return jsonify({'Message': 'Invalid token'}), 403

            return func(*args, **kwargs)

        return decorated

    ### swagger specific ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    ### end swagger specific ###

    # JUST FUNCTIONS
    def dump_or_404(data, Schema):
        if data == 404:
            return Response("Invalid id", status=404)
        else:
            if isinstance(data, list):
                return jsonify(Schema.dump(data, many=True))
            return jsonify(Schema.dump(data))

    # MOVIES ROUTE
    @app.route("/api/v1/movies", methods=['GET'])
    def get_movies():
        args = request.args

        if args != {}:
            response = Movie.get_with_filter(args)
        else:
            response = Movie.get_all()

        return jsonify(MovieSchema().dump(response, many=True))

    @app.route("/api/v1/movies/<id>", methods=['GET'])
    def get_movie(id):
        response = Movie.get_by_id(id)
        return dump_or_404(response, MovieSchema())

    @app.route("/api/v1/movies-preview", methods=['GET'])
    def get_movies_preview():
        args = request.args

        if args != {}:
            response = Movie.get_preview(args)
        else:
            response = Movie.get_preview()

        return jsonify(MoviePreviewSchema().dump(response, many=True))

    @app.route("/api/v1/movies/<id>", methods=['DELETE'])
    @admin_token_required
    def delete_movie(id):
        response = Movie.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/movies", methods=['POST'])
    @admin_token_required
    def post_movie():
        movie_json = MovieSchema().load(request.get_json())
        movie_object = Movie(**movie_json)

        response = Movie.post_one(movie_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/movies/<id>", methods=['PUT'])
    @admin_token_required
    def update_movie(id):
        fields_to_update = MovieSchema().load(request.get_json(), partial=True)

        response = Movie.update_one(id, fields_to_update)
        return Response(f"status: {response}", status=response)

    # SCHEDULED MOVIES ROUTE
    @app.route("/api/v1/scheduledMovies", methods=['GET'])
    def get_scheduledMovies():
        args = request.args

        if args != {}:
            response = ScheduledMovie.get_with_filter(args)
        else:
            response = ScheduledMovie.get_all()

        return jsonify(ScheduledMovieSchema().dump(response, many=True))

    @app.route("/api/v1/scheduledMovies", methods=['POST'])
    # @admin_token_required
    def post_scheduledMovie():
        movie_json = ScheduledMovieSchema().load(request.get_json())
        movie_object = ScheduledMovie(**movie_json)

        response = ScheduledMovie.post_one(movie_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/scheduledMovies/<id>", methods=['DELETE'])
    @admin_token_required
    def delete_scheduledMovie(id):
        response = ScheduledMovie.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/scheduledMovies/<id>", methods=['PUT'])
    @admin_token_required
    def update_cheduledMovie(id):
        fields_to_update = ScheduledMovieSchema().load(request.get_json(), partial=True)

        response = ScheduledMovie.update_one(id, fields_to_update)
        return Response(f"status: {response}", status=response)

    # VIEW TICKET
    @app.route("/api/v1/scheduledMovies/<id>/tickets", methods=['GET'])
    def get_tickets_of_scheduledMovie(id):
        scheduledMovie_object = ScheduledMovie.get_by_id(id)
        if scheduledMovie_object == 404:
            return Response("Invalid id", status=404)
        else:
            return jsonify(TicketSchema().dump(ScheduledMovie.get_tickets(id), many=True))

    # TICKET ROUTE
    @app.route("/api/v1/tickets", methods=['GET'])
    @admin_token_required
    def get_all_tickets():
        response = Ticket.get_all()

        return jsonify(TicketSchema().dump(response, many=True))

    @app.route("/api/v1/tickets/<id>", methods=['GET'])
    @admin_token_required
    def get_ticket_by_id(id):

        response = Ticket.get_by_id(id)

        return dump_or_404(response, TicketSchema())

    @app.route("/api/v1/user/tickets/<id_user>", methods=['GET'])
    @user_token_required
    def get_tickets_of_user(id_user):

        response = Ticket.get_tickets_of_user(id_user)

        return jsonify(TicketSchema().dump(response, many=True))

    @app.route("/api/v1/tickets", methods=['POST'])
    @user_token_required
    def post_ticket():
        ticket_json = TicketSchema().load(request.get_json())
        ticket_object = Ticket(**ticket_json)

        response = Ticket.post_one(ticket_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/tickets/<id>", methods=['DELETE'])
    @admin_token_required
    def delete_ticket(id):
        response = Ticket.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/tickets/<id>", methods=['PUT'])
    @admin_token_required
    def update_ticket(id):
        fields_to_update = TicketSchema().load(request.get_json(), partial=True)

        response = Ticket.update_one(id, fields_to_update)
        return Response(f"status: {response}", status=response)

    # USER ROUTE
    @app.route("/api/v1/users", methods=['GET'])
    @admin_token_required
    def get_user_id():
        args = request.args

        response = User.get_with_filter(args)

        return jsonify(UserSchema().dump(response, many=True))

    @app.route("/api/v1/sign-up", methods=['POST'])
    def create_user():
        user_json = UserSchema().load(request.get_json())
        user_object = User(**user_json)

        response = User.post_one(user_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/log-in", methods=['POST'])
    def login_user():
        user_json = UserSchema().load(request.get_json(), partial=True)
        user = User.auth(user_json['user_name'], user_json['password_hash'])
        if user:
            session['logged_in'] = True

            token = jwt.encode({
                'user': user_json['user_name'],
                'expiration': str(datetime.utcnow() + timedelta(minutes=60 * 24 * 3))
            }, app.config['SECRET_KEY'])

            user.token = token.decode('utf-8')
            return jsonify(UserSchema().dump(user))
        else:
            return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})

    @app.route("/api/v1/users/<id>", methods=['DELETE'])
    @admin_token_required
    def delete_user(id):
        response = User.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    # ADMIN ROUTE
    @app.route('/api/v1/admin', methods=['POST'])
    def login_admin():
        admin_json = request.get_json()
        admin = Admin.auth(admin_json['user_name'], admin_json['password_hash'])
        if admin:
            session['logged_in'] = True

            token = jwt.encode({
                'admin': admin_json['user_name'],
                'expiration': str(datetime.utcnow() + timedelta(minutes=60 * 24 * 1))
            }, app.config['SECRET_KEY'])

            admin.token = token.decode('utf-8')
            return jsonify(AdminSchema().dump(admin))
        else:
            return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed"'})

    # HALL ROUTE
    @app.route('/api/v1/halls', methods=['GET'])
    def get_halls():
        response = Hall.get_all()

        return jsonify(HallSchema().dump(response, many=True))

    @app.route("/api/v1/halls/<hall_name>", methods=['DELETE'])
    @admin_token_required
    def delete_hall(hall_name):
        response = Hall.delete_by_name(hall_name)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/halls", methods=['POST'])
    @admin_token_required
    def post_hall():
        hall_json = HallSchema().load(request.get_json())
        hall_object = Hall(**hall_json)

        response = Hall.post_one(hall_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/halls/<hall_name>", methods=['PUT'])
    @admin_token_required
    def update_hall(hall_name):
        fields_to_update = HallSchema().load(request.get_json(), partial=True)

        response = Hall.update_one(hall_name, fields_to_update)
        return Response(f"status: {response}", status=response)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
