from typing import Dict
import uuid

from singleton import singleton


class City:
    def __init__(self, name: str, pincode: int):
        self.city_id = uuid.uuid4()
        self.name = name
        self.pincode = pincode


@singleton
class CityManager:
    def __init__(self):
        self.city_id_to_city_map: Dict[uuid.UUID, City] = {}

    def add_city(self, city: City):
        if city.city_id in self.city_id_to_city_map:
            raise ValueError(f"City with id {city.city_id} already exists")
        self.city_id_to_city_map[city.city_id] = city

    def remove_city(self, city: City):
        if city.city_id not in self.city_id_to_city_map:
            raise ValueError(f"City with id {city.city_id} doesn't exist")
        self.city_id_to_city_map.pop(city.city_id)
