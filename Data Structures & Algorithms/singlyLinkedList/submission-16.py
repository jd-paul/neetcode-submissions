class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val=0):
        new_node = ListNode(val)
        self.head = None
        self.tail = None
        self.counter = 0 # Starts with one node.
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.counter:
            return -1
        elif index == self.counter - 1:
            return self.tail.val

        current = self.head
        while current and current.next and index > 0:
            current = current.next
            index -= 1
        
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node
        
        self.counter += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        
        self.tail = new_node

        self.counter += 1

    def remove(self, index: int) -> bool:
        if index >= self.counter:
            return False

        # if head? Cannot do the same for tail, need a pointer
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        
        # Now we loop through
        else:
            current = self.head
            counter = 0
            while current:
                if counter+1 == index:
                    if current and current.next:
                        current.next = current.next.next
                    else:
                        current.next = None
                    
                    if current.next is None:
                        self.tail = current
                    break
                else:
                    current = current.next
                    counter += 1
        self.counter -= 1
        return True

    def getValues(self) -> List[int]:
        lst = []
        
        current = self.head
        while current:
            lst.append(current.val)
            current = current.next

        return lst