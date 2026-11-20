
"""
Input: prices = [10,1,5,6,7,1]
    1, 7

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100000000
        max_profit = 0

        for i in prices:
            max_profit = max(max_profit, i - lowest)
            lowest = min(i, lowest)
        
        return max_profit