class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]
        for i in range(1,n):
            if i-2>=0:
                rob = nums[i] + prev2
            else:
                rob = nums[i]
            not_rob = prev
            curr = max(rob,not_rob)
            prev2 = prev         
            prev = curr
        return prev