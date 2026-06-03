class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(heights)-1
        maxArea = -1

        while leftPtr < rightPtr:
            distance = rightPtr - leftPtr
            
            currentArea = distance * min(heights[leftPtr], heights[rightPtr])

            if currentArea > maxArea:
                maxArea = currentArea
        
            # --- #

            if heights[leftPtr] > heights[rightPtr]:
                rightPtr-=1
            else:
                leftPtr+=1
        
        return maxArea