class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]

        for i in range(n):
            if i-2<0:
                take = nums[i]
            else:
                take = dp[i-2] + nums[i]
            not_take = dp[i-1]
            dp[i] = max(take,not_take)
        return dp[n-1]