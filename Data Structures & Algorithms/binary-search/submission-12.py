class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        
        return self.binarySearch(nums, left, right, target)
    
    def binarySearch(self, nums: List[int], left: int, right: int, target: int):
        mid = (left + right) // 2

        if left > right:
            return -1
        
        elif nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, left, mid - 1, target)
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)