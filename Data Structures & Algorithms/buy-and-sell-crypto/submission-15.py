class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Step 1: Update the lowest price seen so far
            if price < min_price:
                min_price = price
            
            # Step 2: Otherwise, see if selling today beats our best profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit