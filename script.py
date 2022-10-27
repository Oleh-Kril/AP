from datetime import datetime, date

from db import *
session = Session()


user1 = User(user_id=1, user_name='Oleg00', full_name='Oleg Kril', token='eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S9A', email='olegkril454464@gmail.com', phone='380547824585')
user2 = User(user_id=2, user_name="Petro45", full_name="Petro Ulon", token="eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S5F", email="unlovfdgd@gmail.com", phone="380578456789")
session.add(user1)
session.add(user2)
session.commit()

language1 = Language(name='Ukrainian')
language2 = Language(name='English')
language3 = Language(name='French')

session.add(language1)
session.add(language2)
session.add(language3)
session.commit()


country1 = Country(name='Ukraine')
country2 = Country(name='USA')
country3 = Country(name='France')

session.add(country1)
session.add(country2)
session.add(country3)
session.commit()


genre1 = Genre(name='Action')
genre2 = Genre(name='Comedy')
genre3 = Genre(name='Fantasy')

session.add(genre1)
session.add(genre2)
session.add(genre3)
session.commit()


director1 = Director(director_id=5, name='John Hamburg')

session.add(director1)
session.commit()


admin1 = Admin(user_name='Oleg00', full_name='Oleg Kril', token='eyJhbGciOiJIUzI1NiJ9')
session.add(admin1)
session.commit()

movie1 = Movie(title='Me Time', poster_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt14309446%2F&psig=AOvVaw0cxBBOg0NcTHbVAd-ek1PA&ust=1666952326633000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCNDk3ryXgPsCFQAAAAAdAAAAABAE', description='Follows a dad who finds time for himself for the first time in years while his wife and kids are away. He reconnects with a friend for a wild weekend.', created_year=date(2022, 1, 1), long=101, age_restriction=16, id_country=2, id_genre=2, id_director=5)
session.add(movie1)
session.commit()

scheduled_movie1 = ScheduledMovie(date_time=datetime(2022, 11, 28, 23, 55, 59, 342380), price=120, hall='3F', type="2D", id_language=1, id_movie=1)
session.add(scheduled_movie1)
session.commit()

ticket1 = Ticket(row_n=1, seat_n=1, id_user=1, id_scheduled_movie=1)
ticket2 = Ticket(row_n=1, seat_n=2, id_user=2, id_scheduled_movie=1)
session.add(ticket1)
session.add(ticket2)
session.commit()

session.close()