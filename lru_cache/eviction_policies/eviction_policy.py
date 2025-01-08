from eviction_policies.lru_eviction_policy import LRUEvictionPolicy
from singleton import singleton


@singleton
class EvictionPolicyStrategy:
    def get_eviction_policy(self):
        return LRUEvictionPolicy()
