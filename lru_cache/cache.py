from typing import Optional

from eviction_policies.base_eviction_policy import EvictionPolicy
from singleton import singleton
from storage.base_storage import Storage


@singleton
class Cache:
    def __init__(
        self, capacity: int, storage: Storage, eviction_policy: EvictionPolicy
    ):
        self.capacity = capacity
        self.storage = storage
        self.eviction_policy = eviction_policy

    def get(self, key: int) -> Optional[int]:
        value = self.storage.get(key)
        if value is not None:
            self.eviction_policy.access_key(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.storage.get_size() == self.capacity:
            _key = self.eviction_policy.evict_key()
            self.storage.remove(_key)
        self.storage.put(key, value)
        self.eviction_policy.access_key(key)
