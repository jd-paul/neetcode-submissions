class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            current_total = numbers[start] + numbers[end]
            if current_total == target:
                return [start+1, end+1]

            elif current_total > target:
                end-=1
            
            else:
                start+=1
            
        return [-1]