class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            # For now, I won't utilise the 'Max-heap' data structure as I'm not familiar with it.

            y = stones.pop()
            x = stones.pop()

            if x != y:
                stones.append(y-x)
            
        if len(stones) == 1:
            return stones[0]
        return 0