class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {} # value, index

        for i, v in enumerate(nums):
            complement = target - v
            if complement in dct:
                return [dct[complement], i]
            dct[v] = i
        
        return []