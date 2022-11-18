import json
import pytest

from db import *
from main import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_insert_movie(client):
    movie = {
        "movie_id" : "0",
        "title": "The Life",
        "poster_url": "http://google.com",
        "created_year": "2004-08-31",
        "long": 178,
        "age_restriction" : 18,
        "country" : "Ukraine",
        "genre" : "Horror",
        "director" : "Unnamed",
        "description" : "This is the time of war with terrible beast from east"
    }

    response = client.post('/api/v1/movies',
                                      json=movie,
                                      headers={"Content-Type": "application/json"})

    assert response.status_code == 200

def test_get_movie(client):
    response = client.get('/api/v1/movies?genre=Horror&director=Unnamed')
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(res) == 1
    assert res[0]["title"] == "The Life"
    global movie_id
    movie_id = res[0]["movie_id"]

def test_update_movie(client):
    updates = {
        "long": 122,
        "age_restriction": 16,
    }

    response = client.put(f'/api/v1/movies/{movie_id}',
                            json=updates,
                            headers={"Content-Type": "application/json"})

    assert response.status_code == 200

def test_delete_movie(client):
    response = client.delete(f'/api/v1/movies/{movie_id}')

    assert response.status_code == 200

def test_get_movies(client):
    response = client.get('/api/v1/movies')
    # res = MovieSchema().loads(response.get_json(), many=True)
    res = json.loads(response.data.decode('utf-8'))

    assert type(res) is list
    assert response.status_code == 200