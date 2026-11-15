class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        We can use binary search. The upper bound of `k` is max(piles).
        Essentially, we use binary search for finding the `k` itself.
        """
        self.piles = piles
        self.h = h
        lower_bound = 1
        upper_bound = max(piles)

        return self.binarySearch(lower_bound, upper_bound)

    def binarySearch(self, l: int, r: int):
        lowest = 1000000000000000
        while l < r:
            k = (l + r) // 2
            if self.checkEating(k):
                lowest = min(lowest, k)
                r = k
            else:
                l = k+1
        
        return l

    def checkEating(self, k: int) -> bool:
        hours = self.h
                
        for b in self.piles:
            hours_needed = b // k + (1 if b % k != 0 else 0)
            hours -= hours_needed
            if hours < 0:
                return False
        
        return True