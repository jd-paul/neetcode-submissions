class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.dct = {}
        self.output = []
        self.recurse([], 0)
        return self.output
    
    def recurse(self, lst: list, index: int):
        key = tuple(lst)
        if key not in self.dct:
            self.dct[key] = 1
            self.output.append(key)
        if index >= len(self.nums):
            return
        
        lst_copy = lst.copy()
        lst_copy.append(self.nums[index])
        
        # Move forward
        self.recurse(lst, index+1)
        self.recurse(lst_copy, index+1)