import threading
import uuid


class Seat:
    def __init__(self):
        self.seat_id = uuid.uuid4()
        self.lock = threading.Lock()
        self.status: str = "AVAILABLE"
