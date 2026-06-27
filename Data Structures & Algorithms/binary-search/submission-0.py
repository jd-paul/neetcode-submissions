class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = ((l + r) // 2) # Round down to the nearest number

            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        
        return -1