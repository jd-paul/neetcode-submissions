class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []

        # simplify it into a twoSum problem
        for i in range(0, len(nums)-1):
            current = nums[i]

            leftPtr = i+1
            rightPtr = len(nums)-1

            while leftPtr < rightPtr:
                opposite_current = nums[leftPtr] + nums[rightPtr]
                
                if opposite_current == -current:
                    new_lst = [current, nums[leftPtr], nums[rightPtr]]
                    if not new_lst in lst:
                        lst.append(new_lst)
                    leftPtr += 1
                elif opposite_current > -current:
                    rightPtr -= 1
                else:
                    leftPtr += 1            
            
        
        return lst