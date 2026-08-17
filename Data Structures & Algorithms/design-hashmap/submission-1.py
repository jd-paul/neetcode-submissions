class MyHashMap:
    """
    Key, value pairs
    lst = [[key, value], [key, value], [key, value]]
    
    sample_lst = [[1,1], [2,2]]

    """
    lst = []

    def __init__(self):
        self.lst = []

    def put(self, key: int, value: int) -> None:
        for sub_lst in self.lst:
            if sub_lst[0] == key:
                sub_lst[1] = value
                return None

        self.lst.append([key, value])

    def get(self, key: int) -> int:
        for sub_lst in self.lst:
            if sub_lst[0] == key:
                return sub_lst[1]
        
        return -1

    def remove(self, key: int) -> None:
        found_the_lst = -1
        for sub_lst in self.lst:
            if sub_lst[0] == key:
                found_the_lst = sub_lst
        
        if found_the_lst != -1:
            self.lst.remove(found_the_lst)        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)