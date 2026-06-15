class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr=[]
        n = len(nums)
        def f(idx):
            if idx == n:
                ans.append(curr.copy())
                return
            #take
            curr.append(nums[idx])
            f(idx+1)
            curr.pop()
            #nottake
            f(idx+1)
        f(0)
        return ans