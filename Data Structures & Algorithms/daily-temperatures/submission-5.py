class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque() # Composed of [temp, index]
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while len(q) >= 1 and temp > q[-1][0]:
                lst = q.pop()
                result[lst[1]] = index - lst[1]
            q.append([temp, index])
        
        return result