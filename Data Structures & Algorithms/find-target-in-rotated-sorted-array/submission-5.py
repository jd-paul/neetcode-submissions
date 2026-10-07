class Solution:
    # Steps: find the pivot
    # Once we established the pivot, we do binary search

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        lst = self.findPivot(nums, target, l, r)
        
        l, r = min(lst), max(lst)

        return self.binarySearch(nums, target, l, r)


    def findPivot(self, nums: List[int], target: int, l: int, r: int) -> List[int]:
        mid = (l + r) // 2

        # if mid + 1 == l or m - 1 == r:
        if nums[l] > nums[mid]:
            if l + 1 == mid:
                # We have two options. Var `target` could be in either of them!
                if target >= nums[0]:
                    return [0, mid]
                return [mid, len(nums)-1]
            else:
                # We have not located the mid here.
                # Do another recursive search with the values here
                return self.findPivot(nums, target, l, mid)
        
        elif nums[mid] > nums[r]:
            # nums[mid] is greater than nums[r], meaning this is where the
            # key is located. We do an initial check first.

            if mid + 1 == r:
                if target >= nums[0]:
                    return [0, mid]
                return [r, len(nums)-1]
            else:
                # We have not located the mid here.
                # Do another recursive search with the values here
                return self.findPivot(nums, target, mid, r)
        
        else:
            return [l, r]

    def binarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        mid = (l + r) // 2
        if l > r:
            return -1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, target, l, mid-1)
        else:
            return self.binarySearch(nums, target, mid + 1, r)