from datetime import datetime, date
from db import *
session = Session()


user1 = User('Oleg00','Oleg Kril', 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S9A',
            'olegkril454464@gmail.com', '380547824585')
user2 = User( "Petro45", "Petro Ulon", "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY2Njg2Mzc4MywiaWF0IjoxNjY2ODYzNzgzfQ.AN3WUMUrS3GentpiEA_ppjOIBCNVkl9hoLGSPuf8S5F",
             "unlovfdgd@gmail.com", "380578456789")
session.add(user1)
session.add(user2)

language1 = Language('Ukrainian')
language2 = Language('English')
language3 = Language('French')

session.add(language1)
session.add(language2)
session.add(language3)


country1 = Country('Ukraine')
country2 = Country('USA')
country3 = Country('France')

session.add(country1)
session.add(country2)
session.add(country3)


genre1 = Genre('Action')
genre2 = Genre('Comedy')
genre3 = Genre('Fantasy')

session.add(genre1)
session.add(genre2)
session.add(genre3)


director1 = Director('John Hamburg')

session.add(director1)


admin1 = Admin('Oleg00', 'Oleg Kril','eyJhbGciOiJIUzI1NiJ9')
session.add(admin1)

movie1 = Movie('Me Time', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt14309446%2F&psig=AOvVaw0cxBBOg0NcTHbVAd-ek1PA&ust=1666952326633000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCNDk3ryXgPsCFQAAAAAdAAAAABAE',
               'Follows a dad who finds time for himself for the first time in years while his wife and kids are away. He reconnects with a friend for a wild weekend.',
               date(2022, 1, 1), 101, 16, 2, 2, 1)
session.add(movie1)

scheduled_movie1 = ScheduledMovie(datetime(2022, 11, 28, 23, 55, 59, 0), 120, '3F',
                                  "2D", 1, 1)
session.add(scheduled_movie1)

ticket1 = Ticket(1, 1, 1, 1)
ticket2 = Ticket(row_n=1, seat_n=2, id_user=2, id_scheduled_movie=1)
session.add(ticket1)
session.add(ticket2)
session.commit()

session.close()