from datetime import datetime

from book_my_show import BookMyShow
from city import City, CityManager
from movie import Movie, MovieManager
from screen import Screen
from seats import Seat
from show import Show, ShowManager
from theatre import Theater, TheaterManager

city = City(pincode=00000, name="Dil-Dil")

city_manager = CityManager()
city_manager.add_city(city)


screen_1 = Screen()
seats = [Seat() for _ in range(100)]
for seat in seats:
    screen_1.add_seat(seat)
theatre = Theater()
theatre.add_screen(screen_1)


theatre_manager = TheaterManager()

movie_manager = MovieManager()
movie = Movie(
    name="Tom and Jerry",
    genre="Cartoon",
    length=100,
    language="As",
    resolution="1900X3456",
)
movie_manager.add_movie(movie)

show = Show(
    theatre.theater_id,
    screen_id=screen_1.screen_id,
    start_time=datetime.now(),
    end_time=datetime.now(),
    movie_id=movie.movie_id,
)
show_manager = ShowManager()
show_manager.add_show(show)

theatre_manager.add_theater(theatre)

book_my_show = BookMyShow()

ticket = book_my_show.book_tickets(
    show.show_id, [seats[0].seat_id, seats[1].seat_id, seats[2].seat_id]
)
print(ticket)
