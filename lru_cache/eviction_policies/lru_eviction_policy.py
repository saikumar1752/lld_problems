from data_structures.double_linked_list import DoubleLinkedList
from data_structures.linked_list_node import LinkedListNode
from eviction_policies.base_eviction_policy import EvictionPolicy


class LRUEvictionPolicy(EvictionPolicy):

    def __init__(self):
        self.d = {}
        self.double_linked_list = DoubleLinkedList()
        self.key_to_node_map = {}

    def evict_key(self) -> int:
        node = self.double_linked_list.remove_tail()
        print("popping key ", node.key)
        self.key_to_node_map.pop(node.key)
        return node.key

    def access_key(self, key: int) -> None:
        if key not in self.key_to_node_map:
            node = LinkedListNode(key)
            self.double_linked_list.add_to_head(node)
            self.key_to_node_map[key] = node
            return
        self.double_linked_list.move_to_head(self.key_to_node_map[key])
