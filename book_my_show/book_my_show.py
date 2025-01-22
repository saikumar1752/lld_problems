from typing import List
from uuid import UUID
from booking_manager import BookingManager
from city import CityManager
from movie import MovieManager
from show import ShowManager
from theatre import TheaterManager
from ticket import TicketManager
from seats import Seat
from singleton import singleton

@singleton
class BookMyShow:
    def __init__(self):
        self.city_manager = CityManager()
        self.booking_manager = BookingManager()
        self.movie_manager = MovieManager()
        self.theater_manager = TheaterManager()
        self.ticket_manager = TicketManager()
        self.show_manager = ShowManager()

    def book_tickets(self, show_id: UUID, seat_ids: List[UUID]) -> bool:
        if not show_id in self.show_manager.show_id_to_show_map:
            raise Exception(f"Show with id: {show_id} doesn't exist")

        show = self.show_manager.show_id_to_show_map[show_id]
        if not show.theater_id in self.theater_manager.theater_id_to_theater_map:
            raise Exception(f"Show is not present in any theater")
        theater = self.theater_manager.theater_id_to_theater_map[show.theater_id]
        print(theater.screen_id_to_screen_map)
        if not show.screen_id not in theater.screen_id_to_screen_map:
            raise Exception(
                f"No screen to play {show_id} in theater {theater.theater_id}"
            )
        screen = theater.screen_id_to_screen_map[show.screen_id]
        seats: List[Seat] = []
        for seat_id in seat_ids:
            if not seat_id in screen.seat_id_to_seat_map:
                raise Exception(f"Seat with id: {seat_id} doesn't exist in screen")
            seats.append(screen.seat_id_to_seat_map[seat_id])
        return self.booking_manager.book_seats(show, seats)
