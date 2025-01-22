from typing import Dict, List
import uuid
from city import City
from seats import Seat
from singleton import singleton


class Ticket:
    def __init__(
        self,
        show_id: uuid.UUID,
        theater_id: uuid.UUID,
        seats: List[Seat],
        screen_id: uuid.UUID,
    ):
        self.ticket_id = uuid.uuid4()
        self.show_id = show_id
        self.theater_id = theater_id
        self.seats = seats
        self.screen_id = screen_id


@singleton
class TicketManager:
    def __init__(self):
        self.ticket_id_to_ticket_map: Dict[str, Ticket] = {}

    def add_ticket(self, ticket: Ticket):
        if ticket.ticket_id in self.ticket_id_to_ticket_map:
            raise Exception(f"Ticket with id: {ticket.ticket_id} already exists")
        self.ticket_id_to_ticket_map[ticket.ticket_id] = ticket

    def remove_ticket(self, ticket: Ticket):
        if ticket.ticket_id not in self.ticket_id_to_ticket_map:
            raise Exception(f"Ticket with id: {ticket.ticket_id} does not exist")
        self.ticket_id_to_ticket_map.pop(ticket.ticket_id)
