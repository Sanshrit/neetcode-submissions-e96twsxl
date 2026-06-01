class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cp = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            min_cp = min(min_cp,prices[i])
            profit = max(profit,prices[i] - min_cp)
        return profit