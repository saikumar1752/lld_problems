from abc import ABC, abstractmethod


class EvictionPolicy(ABC):
    @abstractmethod
    def evict_key(self) -> int:
        pass

    @abstractmethod
    def access_key(self, key: int) -> None:
        pass
