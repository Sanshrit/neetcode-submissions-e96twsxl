class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        curr = []
        def track(idx,n,curr):
            if idx == n:
                ans.append(curr.copy())
                return
            #not take
            track(idx+1,n,curr)    
            #take
            curr.append(nums[idx])
            track(idx+1,n,curr)
            curr.pop()
        track(0,n,curr)
        return ans



        