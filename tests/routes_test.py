import json
from datetime import datetime

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

# AUTH TESTS
def test_log_in_admin(client):
    admin ={
        "user_name": "admin",
        "password_hash": "password"
    }

    response = client.post("/api/v1/admin",
                           json=admin,
                           headers={"Content-Type": "application/json"})

    res = json.loads(response.data.decode('utf-8'))

    assert res["token"] != None
    global token
    token = res["token"]

    fake_admin = {
        "user_name": "alsdfjalkdjfaskjdfdsjfd_user_name",
        "password_hash": "aldsfjkasjjfdjdjfjfj_fake_password"
    }

    response = client.post("/api/v1/admin",
                           json=fake_admin,
                           headers={"Content-Type": "application/json"})

    assert response.status_code == 403

def test_sign_up_user(client):
    user = {
        "user_name": "user",
        "full_name": "User Userovich",
        "password_hash": "password123_hash",
        "email": "someemail@gmail.com",
        "phone": "0988138276"
    }

    response = client.post("/api/v1/sign-up",
                           json=user,
                           headers={"Content-Type": "application/json"})

    assert response.status_code == 200
def test_find_user(client):
    response = client.get("/api/v1/users?user_name=user&phone=0988138276&password_hash=password123_hash",
                          headers={"Content-Type": "application/json", "token": token})
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(res) == 1
    assert res[0]["user_name"] == "user"
    global user_id
    user_id = res[0]["user_id"]
def test_log_in_user(client):
    user = {
        "user_name": "user",
        "password_hash": "password123_hash"
    }

    response = client.post("/api/v1/log-in",
                           json=user,
                           headers={"Content-Type": "application/json"})
    res = json.loads(response.data.decode('utf-8'))
    assert res["token"] != None
    global user_token
    user_token = res["token"]

# MOVIE TESTS
def test_insert_movie(client):
    movie = {
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
                                      headers={"Content-Type": "application/json", "token": token})

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
                            headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200

def test_get_movies(client):
    response = client.get('/api/v1/movies')
    res = json.loads(response.data.decode('utf-8'))

    assert type(res) is list
    assert response.status_code == 200

def test_get_movies_preview(client):
    response = client.get('/api/v1/movies-preview?country=ukraine')

    res = json.loads(response.data.decode('utf-8'))

    assert type(res) is list
    assert res[0].get("long") == None
    assert response.status_code == 200

# HALL TESTS
def test_insert_hall(client):
    global hall_name
    hall_name = "777"

    hall = {
        "hall_name": hall_name,
        "row_amount": 200,
        "seat_amount": 400
    }

    response = client.post('/api/v1/halls',
                                      json=hall,
                                      headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200
def test_update_hall(client):
    updates = {
        "row_amount": 45,
    }

    response = client.put(f'/api/v1/halls/{hall_name}',
                          json=updates,
                          headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200
def test_get_halls(client):
    response = client.get('/api/v1/halls')
    res = json.loads(response.data.decode('utf-8'))

    assert type(res) is list
    assert len(res) >= 1
    assert response.status_code == 200
# SCHEDULED MOVIE TESTS
def test_insert_scheduledMovie(client):
    scheduledMovie = {
        "id_movie" : movie_id,
        "hall_name" : hall_name,
        "language" : "English",
        "type" : "3D",
        "price": 180,
        "date_time": "2022-11-28 12:55:59"
    }

    response = client.post('/api/v1/scheduledMovies',
                                      json=scheduledMovie,
                                      headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200
def test_get_scheduledMovie(client):
    response = client.get(f'/api/v1/scheduledMovies?date_time=2022-11-28+12:55:59')
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(res) == 1
    assert res[0]["price"] == 180
    global scheduledMovie_id
    scheduledMovie_id = res[0]["scheduledmovie_id"]
def test_update_scheduleMovie(client):
    updates = {
        "price": 220
    }

    response = client.put(f'/api/v1/scheduledMovies/{scheduledMovie_id}',
                            json=updates,
                            headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200
# TICKET TESTS

def test_insert_ticket(client):
    ticket = {
        "row_n": 5,
        "seat_n": 25,
        "id_user": user_id,
        "id_scheduledmovie": scheduledMovie_id
    }

    response = client.post("/api/v1/tickets",
                           json=ticket,
                           headers={"Content-Type": "application/json", "token": user_token})
    assert response.status_code == 200

def test_get_tickets_of_user(client):
    response = client.get(f"/api/v1/user/tickets/{user_id}",
                            headers={"token": user_token})

    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(res) == 1
    assert res[0]["seat_n"] == 25
    global ticket_id
    ticket_id = res[0]["ticket_id"]

def test_get_tickets_of_movie(client):
    response = client.get(f"/api/v1/scheduledMovies/{scheduledMovie_id}/tickets")

    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(res) == 1

def update_ticket_by_admin(client):
    updates = {
        "row_n": 12
    }

    response = client.put(f'/api/v1/tickets/{ticket_id}',
                          json=updates,
                          headers={"Content-Type": "application/json", "token": "notValidToken"})

    assert response.status_code == 403
    assert response.json["Message"] == "Invalid token. Please log in again."

    response = client.put(f'/api/v1/tickets/{ticket_id}',
                          json=updates,
                          headers={"Content-Type": "application/json", "token": token})

    assert response.status_code == 200

def test_get_ticket_by_admin(client):
    response = client.get(f'/api/v1/tickets/{ticket_id}',
                          headers={"token": token})
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200


# DELETE ALL
def test_delete_ticket(client):
    response = client.delete(f'/api/v1/tickets/{ticket_id}',
                             headers={"token": user_token})
    assert response.status_code == 403
    assert response.json["Message"] == 'Admin access only!'

    response = client.delete(f'/api/v1/tickets/{ticket_id}',
                             headers={"token": token})
    assert response.status_code == 200
def test_delete_user(client):
    response = client.delete(f'/api/v1/users/{user_id}',
                             headers={"token": token})

    assert  response.status_code == 200

    response = client.delete(f'/api/v1/users/0',
                             headers={"token": token})

    assert response.status_code == 404
def test_delete_scheduledMovie(client):
    response = client.delete(f'/api/v1/scheduledMovies/{scheduledMovie_id}',
                             headers={"token": token})

    assert response.status_code == 200

    response = client.delete(f'/api/v1/scheduledMovie/0',
                             headers={"token": token})

    assert response.status_code == 404
def test_delete_movie(client):
    response = client.delete(f'/api/v1/movies/{movie_id}',
                                headers={"token": token})

    assert response.status_code == 200
def test_delete_hall(client):
    response = client.delete(f'/api/v1/halls/{hall_name}',
                             headers={"token": token})

    assert response.status_code == 200


