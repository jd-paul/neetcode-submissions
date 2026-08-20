class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for current in prices:
            min_price = min(current, min_price)
            profit = current - min_price

            max_profit = max(max_profit, profit)
        
        return max_profit