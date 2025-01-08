from data_structures.linked_list_node import LinkedListNode


class DoubleLinkedList:
    def __init__(self):
        self.head = LinkedListNode(-1)
        self.tail = LinkedListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: LinkedListNode):
        self._add(node)

    def _add(self, node: LinkedListNode):
        _next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = _next
        _next.prev = node

    def _remove(self, node: LinkedListNode):
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev

    def move_to_head(self, node: LinkedListNode):
        self._remove(node)
        self._add(node)

    def remove_tail(self) -> LinkedListNode:
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        self._remove(node)
        return node
