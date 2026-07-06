class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0

        # Iterate through and move the pointers accordingly.

        while left < right:
            # current area = minimum height * distance
            d = right - left
            h = min(heights[left], heights[right])

            current_area = d * h
            max_area = max(current_area, max_area)

            # Hard checks to iterate through
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area