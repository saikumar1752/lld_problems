from datetime import datetime
from typing import Dict
import uuid
from singleton import singleton


class Show:
    def __init__(
        self,
        theater_id: uuid.UUID,
        screen_id: uuid.UUID,
        start_time: datetime,
        end_time: datetime,
        movie_id: uuid.UUID,
    ):
        self.show_id = uuid.uuid4()
        self.start_time = start_time
        self.end_time = end_time
        self.movie_id = movie_id
        self.theater_id = theater_id
        self.screen_id = screen_id


@singleton
class ShowManager:
    def __init__(self):
        self.show_id_to_show_map: Dict[str, Show] = {}

    def add_show(self, show: Show):
        if show.show_id in self.show_id_to_show_map:
            raise Exception(f"Show with id: {show.show_id} already exists")
        self.show_id_to_show_map[show.show_id] = show

    def remove_show(self, show: Show):

        if show.show_id not in self.show_id_to_show_map:
            raise Exception(f"Show with id: {show.show_id} does not exist")
        self.show_id_to_show_map.pop(show.show_id)
