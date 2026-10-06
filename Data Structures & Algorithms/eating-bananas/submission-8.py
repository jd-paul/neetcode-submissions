import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles[i] = number of bananas in the ith pile
            `h` represents the number of hours needed to eat ALL
            the bananas
            `k` represents the bananas-per-hour eating rate. We get
            to decide on this

        Essentially, how slow can my eating rate be while eating
        all the bananas within the minimum time! What we return
        is our `k`

        Get the smallest eating rate `k` that can finish
        within `h` hours.

        Time it takes to finish a pile = math.ceil(x / k)
        """

        maximum_k = max(piles)
        minimum_k = 1
        mid = (minimum_k + maximum_k) / 2

        return self.recursiveCall(piles, h, minimum_k, maximum_k)

    def recursiveCall(self, piles: List[int], h: int, left: int, right: int):
        mid = (left + right) // 2

        if left > right:
            return 10000000000000000
        
        result = self.computeTime(piles, h, mid)
        if result != -1:
            
            return min(result, self.recursiveCall(piles, h, left, mid-1))
        elif result == -1:
            return self.recursiveCall(piles, h, mid+1, right)

    # Given k, compute 
    # Return -1 if it doesn't work
    def computeTime(self, piles: List[int], h: int, k: int):
        # At each loop, consume k bananas in p pile
        time = 0
        for p in piles:
            time += math.ceil(p / k)
        
        if time > h:
            return -1
        
        return k