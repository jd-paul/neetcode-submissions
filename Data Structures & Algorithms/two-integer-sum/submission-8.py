class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        n = len(nums)

        # Build as you go.
        # Key value pair = value, index

        for i in range(0, n):
            current = nums[i]
            complement = target - current

            if complement in dct:
                return [dct[complement], i]
            else:
                dct[current] = i
        
        return [0, 0]