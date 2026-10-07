class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        Utilise the mid idea.

        Keep searching iteratively. Then
        if nums[left] > nums[right], then
        """

        l, r = 0, len(nums)-1 # These are indices

        return self.recursiveSearch(nums, l, r)

    def recursiveSearch(self, nums: List[int], l: int, r: int) -> int:
        mid = (l + r) // 2

        # if mid + 1 == l or m - 1 == r:
        if nums[l] > nums[mid]:
            if l + 1 == mid:
                return nums[mid]
            else:
                # We have not located the mid here.
                # Do another recursive search with the values here
                return self.recursiveSearch(nums, l, mid)
        
        elif nums[mid] > nums[r]:
            # nums[mid] is greater than nums[r], meaning this is where the
            # key is located. We do an initial check first.

            if mid + 1 == r:
                return nums[r]
            else:
                # We have not located the mid here.
                # Do another recursive search with the values here
                return self.recursiveSearch(nums, mid, r)
        
        else:
            return nums[l]