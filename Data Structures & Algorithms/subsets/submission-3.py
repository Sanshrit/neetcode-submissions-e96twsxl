class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        n = len(nums)
        def rec(idx,curr):
            if idx == n:
                ans.append(curr.copy())
                return 
            #take
            curr.append(nums[idx])
            rec(idx+1,curr)
            curr.pop()
            #not-take
            rec(idx+1,curr)
        rec(0,curr)
        return ans
