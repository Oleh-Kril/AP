from datetime import datetime, date
from db import *
session = Session()

# admin1 = Admin('admin', 'Oleh Kril','password')
# session.add(admin1)
#

# hall2 = Hall("44S", 18, 12)
# session.add(hall2)
#
# movie1 = Movie(title='Dark Side', poster_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt14309446%2F&psig=AOvVaw0cxBBOg0NcTHbVAd-ek1PA&ust=1666952326633000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCNDk3ryXgPsCFQAAAAAdAAAAABAE',
#                description='Follows a dad who finds time for himself for the first time in years while his wife and kids are away. He reconnects with a friend for a wild weekend.',
#                created_year=date(2022, 8, 20), long=124, age_restriction=18,
#                country="Ukraine", genre="Horror", director="Some Dude")
# session.add(movie1)
# session.commit()
#
# scheduled_movie1 = ScheduledMovie("2020-11-28 12:55:59", 120, '44S',
#                                   "3D", "Ukrainian", 18)
# session.add(scheduled_movie1)

# user1 = User('Oleglala','Oleg Dudde', 'eyJhbGciOiJIUzI1NiJ9.edfd2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S9A',
#             'olegkril454464@gmail.com', '380547824585')
# user2 = User( "Petro45", "Petro Ulon", "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S5F",
#              "unlovfdgd@gmail.com", "380578456789")
# session.add(user1)
# session.add(user2)


# ticket1 = Ticket(1, 1, 1, id_scheduledmovie=5)
ticket2 = Ticket(row_n=1, seat_n=2, id_user=18, id_scheduledmovie=19)
# session.add(ticket1)
session.add(ticket2)


# #
session.commit()
session.close()

# curl -X "POST" -H "Content-Type: application/json" -d '{
#    "user_name": "admin",
#     "password_hash": "password"
# }' 'http://127.0.0.1:5000/api/v1/admin'

# curl -X "POST" -H "Content-Type: application/json"  -H "token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiUGV0cm80NSIsImV4cGlyYXRpb24iOiIyMDIyLTExLTI0IDExOjU1OjQxLjk3MzM1MSJ9.nGTbmUX8GYrS6EAyJq8gOSX3iOrv_eQRIyoI5g3v86M" -d '{
#     "title": "The Life",
#     "poster_url": "http://google.com",
#     "created_year": "2004-08-31",
#     "long": 178,
#     "age_restriction" : 18,
#     "country" : "Ukraine",
#     "genre" : "Horror",
#     "director" : "Unnamed",
#     "description" : "This is the time of war with terrible beast from east"
# }' 'http://127.0.0.1:5000/api/v1/movies'

# user token: "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiUGV0cm80NSIsImV4cGlyYXRpb24iOiIyMDIyLTExLTI0IDExOjU1OjQxLjk3MzM1MSJ9.nGTbmUX8GYrS6EAyJq8gOSX3iOrv_eQRIyoI5g3v86M"
# admin token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ImFkbWluIiwiZXhwaXJhdGlvbiI6IjIwMjItMTEtMjIgMTE6NTI6MTQuNTE0ODE3In0.HAWCCc4suVLCxGjCrk71MiFn_YcLxTyEFsJSDfXx4IU

# Commads

# pw_hash = bcrypt.generate_password_hash('hunter2')
# bcrypt.check_password_hash(pw_hash, 'hunter2')

# curl -X "POST" -H "Content-Type: application/json" -d '{
#         "id_movie" : "24",
#         "hall_name" : "1B",
#         "language" : "English",
#         "type" : "3D",
#         "price": 180,
#         "data_time": "2022-11-28 12:55:59"
# }' 'http://127.0.0.1:5000/api/v1/scheduledMovies'

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

    # movie = Movie(title="Test Film", poster_url="http://google.com", created_year= date(2022, 8, 20), long=30,
    #               age_restriction=18, country="Ukraine", genre="Horror", director="Unnamed",
    #               description="This is the time of war with terrible beast from east")

# {'created_year': '2022-08-20', 'genre': 'Horror', 'title': 'Test Film', 'director': 'Unnamed', 'trailer_url': None, 'country': 'Ukraine', 'movie_id': None, 'long': 30, 'age_restriction': 18, 'description': 'This is the time of war with terrible beast from east', 'poster_url': 'http://google.com'}