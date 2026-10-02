class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        This is not necessarily the case. You can traverse L->R and for every value, we check if the current one being iterated over is greater than values you are waiting to find an answer to. The invariant here is that the stack contains values in non-increasing order and you can keep popping and updating them this way until the condition is not met anymore

        Essentially, we want our stack to be monotonically decreasing.

        If we find a case where the current number is not in decreasing order,
        then we adjust accordingly
        """

        stack = []
        results = [0] * len(temperatures)
        top = 0
        for index, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                i = stack.pop()
                results[i] = index - i
            
            stack.append(index)
        
        return results