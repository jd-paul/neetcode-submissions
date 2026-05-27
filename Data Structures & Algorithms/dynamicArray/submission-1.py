class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            capacity = 1
        self.capacity = capacity
        self.size = 0
        self.lst = [None] * capacity

    def get(self, i: int) -> int:
        return self.lst[i]

    # Assume `i` is valid. Assume that the data structure is contiguous.    
    def set(self, i: int, n: int) -> None:  
        self.lst[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()

        self.set(self.size, n)
        self.size += 1
        
    def popback(self) -> int:
        n = self.lst[self.size-1]
        self.size -= 1
        return n
 
    def resize(self) -> None:
        newLst = [None] * self.capacity * 2
        
        for i in range(0, self.capacity):
            newLst[i] = self.lst[i]
        
        self.lst = newLst
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity