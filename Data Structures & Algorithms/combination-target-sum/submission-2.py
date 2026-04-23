class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        n = len(nums)
        def trav(idx,n,curr,target):
            if idx == n:
                if target == 0:
                    ans.append(curr.copy())
                return 
            if nums[idx] <= target:
                curr.append(nums[idx])
                trav(idx,n,curr,target-nums[idx])
                curr.pop()
            trav(idx+1,n,curr,target)
        trav(0,n,curr,target)
        return ans

        