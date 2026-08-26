class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0

        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                counter += 1
        
        return counter
        