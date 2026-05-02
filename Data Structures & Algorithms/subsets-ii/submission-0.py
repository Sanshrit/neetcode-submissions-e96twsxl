class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        curr = []
        ans = []
        nums.sort()
        def f(idx, curr, ans):
            ans.append(curr.copy())
            for i in range(idx,n):
                if idx!=i and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                f(i+1,curr,ans)
                curr.pop()
        f(0,curr,ans)
        return ans