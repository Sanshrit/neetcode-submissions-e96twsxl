class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def f(arr):
            n = len(arr)
            dp = [-1 for _ in range(n)]
            dp[0] = arr[0]            
            for i in range(1,n):
                if i>=2:
                    rob = arr[i] + dp[i-2]
                else:
                    rob = arr[i]
                not_rob = dp[i-1]
                dp[i] = max(rob,not_rob)
            return dp[n-1]
        a1,a2 = [],[]
        for i in range(n):
            if i!=0:
                a1.append(nums[i])
            if i!=n-1:
                a2.append(nums[i])
        return max(f(a1),f(a2))
        