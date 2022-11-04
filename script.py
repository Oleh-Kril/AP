from datetime import datetime, date
from db import *
session = Session()

# admin1 = Admin('Oleg00', 'Oleg Kril','eyJhbGciOiJIUzI1NiJ9')
# session.add(admin1)

# movie1 = Movie(title='Dark Side', poster_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt14309446%2F&psig=AOvVaw0cxBBOg0NcTHbVAd-ek1PA&ust=1666952326633000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCNDk3ryXgPsCFQAAAAAdAAAAABAE',
#                description='Follows a dad who finds time for himself for the first time in years while his wife and kids are away. He reconnects with a friend for a wild weekend.',
#                created_year=date(2022, 8, 20), long=124, age_restriction=18,
#                country="Ukraine", genre="Horror", director="Some Dude")
# session.add(movie1)
#
# scheduled_movie1 = ScheduledMovie(datetime(2022, 11, 28, 12, 55, 59, 0), 120, '1B',
#                                   "3D", "Ukrainian", 1)
# session.add(scheduled_movie1)

# user1 = User('Oleg00','Oleg Kril', 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S9A',
#             'olegkril454464@gmail.com', '380547824585')
# user2 = User( "Petro45", "Petro Ulon", "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S5F",
#              "unlovfdgd@gmail.com", "380578456789")
# session.add(user1)
# session.add(user2)


# ticket1 = Ticket(1, 1, 1, id_scheduledmovie=5)
# ticket2 = Ticket(row_n=1, seat_n=2, id_user=2, id_scheduledmovie=5)
# session.add(ticket1)
# session.add(ticket2)

# hall1 = Hall("3F", 15, 10)
# hall2 = Hall("1B", 18, 12)
# session.add(hall2)
#
# session.commit()
# session.close()