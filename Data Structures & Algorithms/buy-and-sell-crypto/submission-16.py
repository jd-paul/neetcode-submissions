class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1000
        lowest = 1000


        left, right = 0, len(prices)-1

        while left < right:
            left_value = prices[left]
            right_value = max(prices[left:])
            current_profit = right_value - left_value
            profit = max(profit, current_profit)

            left += 1
        
        return max(profit, 0)