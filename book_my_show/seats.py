import threading
import uuid


class Seat:
    def __init__(self):
        self.id = uuid.uui4()
        self.lock=threading.Lock()