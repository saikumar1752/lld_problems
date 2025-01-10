from singleton import singleton
from storage.hash_map_storage import HashMapStorage


@singleton
class StorageStrategy:
    def get_storage(self):
        return HashMapStorage()
