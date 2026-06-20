class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []
        def f(idx,target,curr):
            if idx == n:
                if target == 0:
                    ans.append(curr.copy())
                return
            
            if nums[idx] <= target:
                curr.append(nums[idx])
                f(idx,target-nums[idx],curr)
                curr.pop()
            f(idx+1,target,curr)
        f(0,target,curr)
        return ans
            
            


