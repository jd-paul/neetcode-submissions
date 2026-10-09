class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)

        max_profit = 0
        lowest_price = 100000000

        while l < n:
            

            current_profit = prices[l] - lowest_price
            max_profit = max(max_profit, current_profit)

            lowest_price = min(lowest_price, prices[l])
            l+=1

        return max_profit