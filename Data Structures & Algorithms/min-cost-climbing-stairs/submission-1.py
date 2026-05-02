class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n)]
        def f(idx):
            if idx == 0 or idx == 1:
                return cost[idx]
            if dp[idx]!=-1:
                return dp[idx]
            left = f(idx - 1) + cost[idx]
            right = float('inf')
            if idx >=2:
                right = f(idx-2) + cost[idx]
            dp[idx] = min(left,right)
            return dp[idx]
        
        
        return min(f(n-1),f(n-2))