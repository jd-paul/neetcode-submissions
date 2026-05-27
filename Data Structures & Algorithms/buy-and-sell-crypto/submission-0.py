class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time O(n), space O(1)

        best_profit = -1000
        lowest = 1000

        for idx, value in enumerate(prices):
            if value < lowest:
                lowest = value

            else: # move on
                current_profit = value - lowest
                if current_profit >= best_profit: # check
                    best_profit = current_profit
                else:
                    # move on
                    continue

        if best_profit < 0:
            return 0
        return best_profit