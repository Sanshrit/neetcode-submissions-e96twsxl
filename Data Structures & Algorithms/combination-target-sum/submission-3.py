class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        curr = []
        ans = []
        def trav(idx,curr,target):
            if idx == n:
                if target == 0:
                    ans.append(curr.copy())
                return 
            if target >= nums[idx]:
                curr.append(nums[idx])
                trav(idx,curr,target - nums[idx])
                curr.pop()
            trav(idx+1,curr,target)
            
        trav(0,curr,target)
        return ans