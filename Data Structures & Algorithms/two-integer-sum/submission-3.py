class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        # build the dictionary as you go

        for idx, value in enumerate(nums):
            complement = target - value
            if complement in dct:
                return [dct[complement], idx]
            
            if value not in dct:
                dct[value] = idx
        
        return [0]