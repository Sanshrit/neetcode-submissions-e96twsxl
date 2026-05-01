class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        def f(idx):
            if idx < 0:
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            pick = nums[idx] + f(idx-2)
            not_pick = f(idx-1)
            dp[idx] = max(pick,not_pick)
            
            return dp[idx]

        
        return f(len(nums)-1)
        

        