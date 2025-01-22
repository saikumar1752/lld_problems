from typing import Dict
from uuid import UUID, uuid4

from screen import Screen
from singleton import singleton


class Theater:
    def __init__(self):
        self.screen_id_to_screen_map: Dict[UUID, Theater] = {}
        self.theater_id = uuid4()

    def add_screen(self, screen: Screen):
        if screen.screen_id in self.screen_id_to_screen_map:
            raise Exception(f"Screen with id: {screen.screen_id} already exists!")
        print("adding screen ", screen.screen_id)
        self.screen_id_to_screen_map[screen.screen_id] = screen

    def remove_screen(self, screen: Screen):
        if screen.screen_id not in self.screen_id_to_screen_map:
            raise Exception(f"Screen with id: {screen.screen_id} does not exist!")
        self.screen_id_to_screen_map.pop(screen.screen_id)


@singleton
class TheaterManager:
    def __init__(self):
        self.theater_id_to_theater_map: Dict[UUID, Theater] = {}

    def add_theater(self, theater: Theater):
        if theater.theater_id in self.theater_id_to_theater_map:
            raise Exception(f"Theater with id: {theater.theater_id} already exists")
        self.theater_id_to_theater_map[theater.theater_id] = theater

    def remove_theater(self, theater: Theater):
        if theater.theater_id not in self.theater_id_to_theater_map:
            raise Exception(f"Theater with id: {theater.movie_id} does not exist")
        self.theater_id_to_theater_map.pop(theater.theater_id)
