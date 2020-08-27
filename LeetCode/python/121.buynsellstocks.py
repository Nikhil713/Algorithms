class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        lowest = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            lowest = min(lowest,prices[i])
            profit = max(profit,prices[i] - lowest)
        return profit