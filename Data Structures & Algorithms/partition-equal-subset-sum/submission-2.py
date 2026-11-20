"""
NeetCode guide

for t in subarray:
    if t = target:
        True

    # Given an input array, we will add the totals we obtain to a set.
    # It will act as our hashmap to only get unique values.

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for i in range(0, len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        
        return True if target in dp else False

