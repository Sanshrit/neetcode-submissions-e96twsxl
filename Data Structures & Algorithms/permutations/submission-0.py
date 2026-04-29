class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr= []
        freq = [0 for _ in range(n)]
        def f(idx,curr,ans,freq):
            if idx == n:
                ans.append(curr.copy())
                return
            for i in range(n):
                if freq[i] == 0:
                    curr.append(nums[i])
                    freq[i] = 1
                    f(idx+1,curr,ans,freq)
                    curr.pop()
                    freq[i] = 0
        f(0,curr,ans,freq)
        return ans