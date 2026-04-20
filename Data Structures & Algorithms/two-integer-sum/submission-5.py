class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i in range(len(nums)):
            if target - nums[i] in d1:
                return [d1[target - nums[i]],i]
            else:
                d1[nums[i]] = i
        return [-1,-1]