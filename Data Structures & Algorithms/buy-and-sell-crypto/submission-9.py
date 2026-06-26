class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_cp = prices[0]
        for i in range(1,len(prices)):
            ans = max(ans,prices[i] - min_cp)
            min_cp = min(min_cp,prices[i])
        return ans