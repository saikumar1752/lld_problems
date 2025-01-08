from abc import abstractmethod


class Storage:

    @abstractmethod
    def put(self, key: int, value: int):
        pass

    @abstractmethod
    def get(self, key: int) -> int:
        pass

    @abstractmethod
    def remove(self, key: int):
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
