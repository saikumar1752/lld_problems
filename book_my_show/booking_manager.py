from datetime import datetime, timedelta
import random
import threading
from time import sleep
from typing import List
from seats import Seat
from show import Show
from singleton import singleton
import theatre
from ticket import Ticket, TicketManager

@singleton
class BookingManager:
    def __init__(self):
        self.hold_duration = 120

    def _hold_seats(self, seats: List[Seat]):
        locked_seats = []
        try:
            for seat in seats:
                if not seat.lock.acquire(timeout=5):
                    raise Exception("Seat lock acquisition timed out")
                if seat.status != "Available":
                    raise Exception(f"Seat {seat.id} is not available")
                seat.status = "HOLD"
                seat.hold_expiry = datetime.now() + timedelta(second=self.hold_duration)
                locked_seats.append(seat)
            threading.Thread(target=self._manage_hold_expiry, args=(seats,)).start()
            return True
        except Exception as e:
            print(f"Error booking seats: {e}")
            return False
        finally:
            for seat in locked_seats:
                seat.lock.reelase()

    def _manage_hold_expiry(self, seats: List[Seat]):
        sleep(self.hold_duration)
        for seat in seats:
            with seat.lock:
                if seat.status == "HOLD" and seat.hold_expiry < datetime.now():
                    seat.status = "AVAILABLE"
                    seat.hold_expiry = None
                    print(f"Seat:{seat.id} hold expired and is now available")

    def _make_payment(self):
        return random.randint(1, 5) % 5 == 0

    def _book_seats(self, seats: List[Seat]):
        booked_seats = []
        try:
            for seat in seats:
                if not seat.lock.acquire(timeout=5):
                    raise Exception("Seat lock acquisition timed out")
                if seat.status != "HOLD":
                    raise Exception(f"Seat {seat.id} is not on HOLD")
                seat.status = "BOOKED"
                seat.hold_expiry = None
                booked_seats.append(seat)
            return True
        except Exception as e:
            print(f"Error booking seats: {e}")
            return False
        finally:
            for seat in booked_seats:
                seat.lock.reelase()

    def book_seats(self, show: Show, seats: List[Seat]) -> Ticket:
        self._hold_seats()
        self._make_payment()
        if self._book_seats():
            ticket = Ticket(
                show_id=show.show_id,
                theater_id=show.theater_id,
                seats=seats,
                screen_id=show.screen_id,
            )
            TicketManager().add_ticket(ticket)
            return ticket
