class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 1001
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] < mini:
                mini = nums[mid]
            
            if nums[low] < nums[mid]:
                if nums[low] < mini:
                    mini = nums[low]
                low = mid+1
            else:
                mini = min(mini,nums[high])
                high = mid-1
        return mini