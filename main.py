from flask import Flask


def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/api/v1/hello-world-12")
    def index():
        return f"Hello World, 12"

    return app

# 127.0.0.1:5000/api/v1/hello-world-12
