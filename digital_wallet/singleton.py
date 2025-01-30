import threading
from typing import Dict, Type


def singleton(cls: Type):
    instance_map: Dict[Type, object] = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instance_map:
            with lock:
                if cls not in instance_map:
                    instance_map[cls] = cls(*args, **kwargs)
        return instance_map[cls]

    return get_instance
