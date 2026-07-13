"""
nums = [-1,0,2,4,6,8], target = 4
We initialize with l = 0, r = 5

Obtain the middle. In this case, it becomes 2.
If middle < target, adjust the left / right values accordingly.

[-1,0,2,4,6,8]

l, r = 0, 5
middle = 0 + 5 // 2 = 2

l, r = 2, 5
middle = 2 + 5 // 2 = 3

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = left + ((right - left) // 2)

            middle_num = nums[middle]

            # if nums[left] == target:
            #     return left
            # elif nums[right] == target:
            #     return right
            if nums[middle] == target:
                return middle
            
            elif middle_num > target:
                right = middle - 1

            else:
                left = middle + 1

        return -1