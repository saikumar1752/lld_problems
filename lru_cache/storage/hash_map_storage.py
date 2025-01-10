from abc import abstractmethod
from typing import Optional

from storage.base_storage import Storage


class HashMapStorage(Storage):
    def __init__(self):
        self._map = {}

    def put(self, key: int, value: int):
        self._map[key] = value

    def get(self, key: int) -> Optional[int]:
        return self._map.get(key)

    def remove(self, key: int):
        if key not in self._map:
            raise KeyError(f"Key `{key}` does not exist")
        self._map.pop(key)

    def get_size(self):
        return len(self._map)
