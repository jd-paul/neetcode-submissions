"""
Two data structures
Dictionary
LinkedList
    - Will be used for deletions (Deleting tail, creating head)
    - This will be composed of indices
"""

class Node:
    def __init__(self, key: int = 0):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.actualCapacity = 0
        
        self.dct = {}
        self.tail = None
        self.head = None

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1

        # We need to make the selected key the most recently used!
        node = self.dct[key][1]
        self._move_to_front(node)

        return self.dct[key][0]

    def _move_to_front(self, node) -> None:
        if node == self.head:
            return
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev if node.prev else node.next
        
        self.head.next = node
        node.prev = self.head
        node.next = None
        self.head = node

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct[key][0] = value
            self._move_to_front(self.dct[key][1])
            return

        newNode = Node(key)
        prev = self.head
        if len(self.dct) == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.head = newNode
            prev.next = self.head
            self.head.prev = prev
        
        if self.actualCapacity >= self.capacity:
            prev_tail = self.tail
            self.tail = self.tail.next
            self.tail.prev = None
            del self.dct[prev_tail.key]
            self.actualCapacity -= 1
        
        self.actualCapacity += 1
        self.dct[key] = [value, newNode]