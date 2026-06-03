class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            leftPtr = i+1
            rightPtr = len(nums) - 1

            while leftPtr < rightPtr:
                total = nums[i] + nums[leftPtr] + nums[rightPtr]
                
                if total == 0:
                    triplets.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    # Skip duplicates for leftPtr
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr + 1]:
                        leftPtr += 1
                    # Skip duplicates for rightPtr  
                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr - 1]:
                        rightPtr -= 1
                    leftPtr += 1
                    rightPtr -= 1
                elif total < 0:
                    leftPtr += 1
                else:
                    rightPtr -= 1

        return triplets