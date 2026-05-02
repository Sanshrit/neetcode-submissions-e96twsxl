class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        def f(idx):
            if idx == 0:
                return nums[idx]
            if dp[idx]!=-1:
                return dp[idx]
            not_rob = f(idx-1)
            rob = nums[idx]
            if idx>=2:
                rob = nums[idx] + f(idx-2)
            dp[idx] = max(rob,not_rob)
            return dp[idx]
        return f(n-1)