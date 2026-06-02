class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ptrStart = 0
        ptrEnd = len(numbers)-1

        while ptrEnd > ptrStart:
            if numbers[ptrStart] + numbers[ptrEnd] == target:
                break

            elif numbers[ptrStart] + numbers[ptrEnd] > target:
                ptrEnd-=1
            
            elif numbers[ptrStart] + numbers[ptrEnd] < target:
                ptrStart+=1

        return [ptrStart+1, ptrEnd+1]