class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j, k = 0, 1
        max_sum = 0

        lowest = max(prices)
        highest = min(prices)

        if len(prices) == 1:
            return 0

        while k < len(prices):
            current_sum = prices[k] - prices[j]

            if current_sum >= max_sum:
                max_sum = current_sum

            if prices[k] > prices[j]:
                k+=1
            elif prices[j] >= prices[k]:
                j=k
                k+=1
        
        return max_sum
                