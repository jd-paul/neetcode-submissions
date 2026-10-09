class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        parked_point = 0
        lowest = 1000000000000000
        max_profit = -1000000000000000

        for index, value in enumerate(prices):
            profit = value - lowest

            max_profit = max(profit, max_profit, 0)
            lowest = min(value, lowest)
        
        return max_profit