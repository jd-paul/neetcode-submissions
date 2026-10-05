class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Should only contain indices
        results = [0] * len(temperatures)
        n = len(temperatures)

        """
        At the moment you process index i, what should the stack contain — and in what order?
        In particular: when you look at temperatures[i],
        which entries in the stack are useless to you and deserve to be popped?
        """

        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                results[i] = stack[-1] - i
            
            stack.append(i)
        
        return results