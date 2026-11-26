class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.res = -1
    
        def recurse(l: int, r: int):
            mid = (l + r) // 2
            if l > r:
                return

            if nums[mid] == target:
                self.res = mid
                return True
            elif nums[mid] > target:
                return recurse(l, mid-1)
            elif nums[mid] < target:
                return recurse(mid+1, r)
        
        recurse(0, len(nums)-1)
        return self.res