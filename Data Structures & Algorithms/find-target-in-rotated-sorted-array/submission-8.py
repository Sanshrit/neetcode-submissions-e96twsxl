class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            
            # find sorted half
            #left half sorted
            if nums[low] <= nums[mid]:
                # is target in range
                if nums[low] <= target and target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            # rigth half sorted
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1



        