from cache import Cache
from eviction_policies.eviction_policy import EvictionPolicyStrategy
from storage.storage import StorageStrategy

storage = StorageStrategy().get_storage()
eviction_policy = EvictionPolicyStrategy().get_eviction_policy()
cache = Cache(capacity=5, storage=storage, eviction_policy=eviction_policy)

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
cache.put(4, 40)
cache.put(5, 50)
cache.put(6, 60)
cache.put(7, 70)
