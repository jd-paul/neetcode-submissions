"""
result = []
    number of days after ith before a warmer temperature appears
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        result = [0] * len(temperatures)

        for index, curr in enumerate(temperatures):
            while q and temperatures[q[-1]] < curr:
                top = q[-1]
                result[top] = index - top
                q.pop()
            q.append(index)
            
        return result