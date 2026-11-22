class Solution:
    """
    stonmes[i] = weight of ith stone

    At each step, we choose the two heaviest stones,
    with weight x and y. Smash them together.
        x == y: destroy and pop both
        if x < y:
            x is destroyed. y's new eight = y - x
        
    Continue until there is only one stone left.
    Return the weight of the last remaining stone or return 0 if none remain.
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, value in enumerate(stones):
            stones[index] = -value
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, -(y - x))
            else:
                heapq.heappush(stones, -(x - y))

        if len(stones) == 1:
            return -stones[0]
        return 0