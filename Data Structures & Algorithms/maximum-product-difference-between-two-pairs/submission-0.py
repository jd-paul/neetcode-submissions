class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        a, b = nums[n-1], nums[n-2]
        c, d = nums[0], nums[1]

        return (a*b - c*d)