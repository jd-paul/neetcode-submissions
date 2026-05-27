class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        # build the dictionary as you go
        for index, val in enumerate(nums):
            c = target - val # complement
            if c in dct:
                return [dct[c], index]


            if val not in dct:
                dct[val] = index
            
            else:
                if c in dct:
                    return [dct[c], index]
        
        return [0, 0]