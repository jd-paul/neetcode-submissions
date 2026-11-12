class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.recurse(0)
    
    def recurse(self, i):
        if i >= len(self.nums):
            return 0

        if i in self.memo:
            return self.memo[i]
        
        # Two cases: Either skip or add this number
        self.memo[i] = self.nums[i] + self.recurse(i+2)
        return max(
            self.recurse(i+1), # Skip
            self.memo[i]
        )