class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        return self.recursiveSearch(nums, target, l, r)
    
    def recursiveSearch(self, nums: List[int], target: int, left: int, right: int):
        # l, r, and mid are indices
        mid = (left + right) // 2

        if left > right or right < left:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.recursiveSearch(nums, target, left, mid-1)
        elif nums[mid] < target:
            return self.recursiveSearch(nums, target, mid+1, right)
        else:
            return -1