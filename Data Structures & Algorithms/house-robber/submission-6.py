class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        for i in range(n):
            if i-2 <0:
                rob = nums[i]
            else:
                rob = nums[i] + dp[i-2]
            
            not_rob = dp[i-1]
            dp[i] = max(rob,not_rob)
        return dp[n-1]