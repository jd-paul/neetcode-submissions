class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.recurse(0, float('-inf'))

    def recurse(self, index: int, prev: int):
        if index == len(self.nums):
            return 0

        if (index, prev) in self.memo:
            return self.memo[(index, prev)]
        
        skip = self.recurse(index + 1, prev)
        
        if self.nums[index] > prev:
            take = 1 + self.recurse(index + 1, self.nums[index])
        else:
            take = 0

        self.memo[(index, prev)] = max(skip, take)
        return self.memo[(index, prev)]