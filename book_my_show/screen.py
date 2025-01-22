from typing import Dict
from uuid import UUID, uuid4

from seats import Seat


class Screen:
    def __init__(self):
        self.seat_id_to_seat_map: Dict[UUID, Seat] = {}
        self.screen_id = uuid4()

    def add_seat(self, seat: Seat):
        if seat.seat_id in self.seat_id_to_seat_map:
            raise Exception(f"Seat with id: {seat.seat_id} already exists")
        self.seat_id_to_seat_map[seat.seat_id] = seat

    def remove_seat(self, seat: Seat):
        if seat.seat_id not in self.seat_id_to_seat_map:
            raise Exception(f"Seat with id: {seat.seat_id} does not exist")
        self.seat_id_to_seat_map.pop(seat.seat_id)
