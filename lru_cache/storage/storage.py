from storage.hash_map_storage import HashMapStorage
from singleton import singleton


@singleton
class StorageStrategy:
    def get_storage(self):
        return HashMapStorage()
