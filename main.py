
from flask import Flask, jsonify, request, Response
from db import *
from flask_swagger_ui import get_swaggerui_blueprint

def create_app(testing: bool = True):
    app = Flask(__name__)

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
    @app.route("/api/v1/movies-preview/<id>", methods=['GET'])
    def get_movie_preview(id):
        response = Movie.get_preview(id)
        return dump_or_404(response, MovieSchema())
    @app.route("/api/v1/movies/<id>", methods=['DELETE'])
    def delete_movie(id):
        response = Movie.delete_by_id(id)
        return Response(f"Status: {response}" , status=response)
    @app.route("/api/v1/movies", methods=['POST'])
    def post_movie():
        movie_json = MovieSchema().load(request.get_json())
        movie_object = Movie(**movie_json)

        response = Movie.post_one(movie_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/movies/<id>", methods=['PUT'])
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
    def post_scheduledMovie():
        movie_json = ScheduledMovieSchema().load(request.get_json())
        movie_object = ScheduledMovie(**movie_json)

        response = ScheduledMovie.post_one(movie_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/scheduledMovies/<id>", methods=['DELETE'])
    def delete_scheduledMovie(id):
        response = ScheduledMovie.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/scheduledMovies/<id>", methods=['PUT'])
    def update_cheduledMovie(id):
        fields_to_update = ScheduledMovieSchema().load(request.get_json(), partial=True)

        response = ScheduledMovie.update_one(id, fields_to_update)
        return Response(f"status: {response}", status=response)

    # BUY TICKET
    @app.route("/api/v1/scheduledMovies/<id>/tickets", methods=['GET'])
    def get_tickets_of_scheduledMovie(id):
        scheduledMovie_object = ScheduledMovie.get_by_id(id)
        if scheduledMovie_object == 404:
            return Response("Invalid id", status=404)
        else:
            return jsonify(TicketSchema().dump(ScheduledMovie.get_tickets(id), many=True))
    # TICKET ROUTE
    @app.route("/api/v1/tickets", methods=['GET'])
    def get_all_tickets():
        response = Ticket.get_all()

        return jsonify(TicketSchema().dump(response, many=True))
    @app.route("/api/v1/tickets/<id>", methods=['GET'])
    def get_ticket_by_id(id):

        response = Ticket.get_by_id(id)

        return dump_or_404(response, TicketSchema())

    @app.route("/api/v1/user/tickets/<id_user>", methods=['GET'])
    def get_tickets_of_user(id_user):

        response = Ticket.get_tickets_of_user(id_user)

        return jsonify(TicketSchema().dump(response, many=True))

    @app.route("/api/v1/tickets", methods=['POST'])
    def post_ticket():
        ticket_json = TicketSchema().load(request.get_json())
        ticket_object = Ticket(**ticket_json)

        response = Ticket.post_one(ticket_object)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/tickets/<id>", methods=['DELETE'])
    def delete_ticket(id):
        response = Ticket.delete_by_id(id)
        return Response(f"Status: {response}", status=response)

    @app.route("/api/v1/tickets/<id>", methods=['PUT'])
    def update_ticket(id):
        fields_to_update = TicketSchema().load(request.get_json(), partial=True)

        response = Ticket.update_one(id, fields_to_update)
        return Response(f"status: {response}", status=response)

    # USER ROUTE
    @app.route("/api/v1/users", methods=['POST'])
    def create_user():
        user_json = UserSchema().load(request.get_json())
        user_object = User(**user_json)

        response = User.post_one(user_object)
        return Response(f"Status: {response}", status=response)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

# Commads

# pw_hash = bcrypt.generate_password_hash('hunter2')
# bcrypt.check_password_hash(pw_hash, 'hunter2')

# curl -X "POST" -H "Content-Type: application/json" -d '{
#     "id_user": 1,
#     "row_n": 2,
#     "seat_n": 1,
#     "id_scheduledmovie": 5
# }' 'http://127.0.0.1:5000/api/v1/tickets'

# curl 'http://127.0.0.1:5000/api/v1/scheduledMovies/5/tickets'

# curl -X "DELETE" "http://127.0.0.1:5000/api/v1/movies/2"

# curl -X "PUT" -H "Content-Type: application/json" \
# -d '{
#     "seat_n": 5
# }' 'http://127.0.0.1:5000/api/v1/tickets/1'

# curl 'http://127.0.0.1:5000/api/v1/movies'
# curl 'http://127.0.0.1:5000/api/v1/movies?genre=horror&director=Dude&title=Dark'
# User()
# {
#     "user_name": "user",
#     "full_name": "User Userovich",
#     "token": "password123",
#     "email": "someemail@gmail.com",
#     "phone": "0988138276"
# }