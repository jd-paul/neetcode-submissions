class Solution:
    def rob(self, nums: List[int]) -> int:
        # Tree functionality
        self.nums = nums
        houseMap = {}
        
        lst = []
        for i in range(0, len(nums)):
            total = nums[i]
            houseMapCopy =  houseMap.copy()
            houseMapCopy[i] = True
            if i-1 >= 0:
                houseMapCopy[i-1] = True
            if i+1 < len(nums):
                houseMapCopy[i+1] = True
            
            lst.append(self.recurse(houseMapCopy, total))

        return max(lst)

            
    # Hit a house, then mark those options as hit.
    def recurse(self, houseMap: dict, total: int) -> int:
        
        # Iterate through
        for i in range(0, len(self.nums)):
            if i in houseMap:
                continue
            
            total += self.nums[i]
            houseMapCopy =  houseMap.copy()
            houseMapCopy[i] = True
            if i-1 >= 0:
                houseMapCopy[i-1] = True
            if i+1 < len(self.nums):
                houseMapCopy[i+1] = True
            
            return self.recurse(houseMapCopy, total)

        return total