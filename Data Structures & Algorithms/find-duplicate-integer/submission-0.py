class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 0

        current = i
        while current < len(nums)-1:
            n = nums[current]
            prev = current
            current = nums[n]
            if current == prev:
                return current
        
        return current
            
