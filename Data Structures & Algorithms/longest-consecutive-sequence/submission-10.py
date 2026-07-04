class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the length of the
        longest consecutive sequence of elements that can be formed.
        """

        # Hard checks
        if len(nums) == 0 or nums is None:
            return 0
        elif len(nums) == 1:
            return 1

        # Initialise
        nums.sort()
        total_max = 0
        accumulation = 0
        n = len(nums)

        prev = nums[0]
        for i in range(1, n):
            current = nums[i]

            # Check if consecutive
            if prev == current:
                accumulation += 0
            elif prev + 1 == current:
                accumulation += 1
            else:
                accumulation = 0
            
            # Check if we've reached longest
            total_max = max(total_max, accumulation)

            # Get `prev` ready
            prev = current
        
        return total_max + 1