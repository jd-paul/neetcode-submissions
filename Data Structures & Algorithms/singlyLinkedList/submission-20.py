class Node:

    def __init__(self, value):
        self.next = None
        self.val = value

class LinkedList:
    
    def __init__(self):      
        self.head = None
        self.tail = None

    # void insertHead(int val) will insert a node with val at the head of the list.
    def insertHead(self, val: int) -> None:
        if self.head is None and self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, val: int) -> None:
        if self.head is None and self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode

    # int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    def get(self, index: int) -> int:
        curr = self.head
        counter = 0

        while curr is not None:
            if counter == index:
                break
            curr = curr.next
            counter += 1

        if curr is None:
            return -1
        return curr.val

    def remove(self, index: int) -> bool:
        curr = self.head
        counter = 0

        prev = None

        while curr is not None:
            if counter == index:
                break

            prev = curr
            curr = curr.next
            counter += 1
        
        if curr is None:
            return False

        if prev is None:
            self.head = curr.next

            if curr.next is None:
                self.tail = None
            return True

        if curr.next is None:
            self.tail = prev
        
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        lst = []

        curr = self.head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next

        return lst