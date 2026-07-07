class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def trav(low,high,target):
            if low > high:
                return -1
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return trav(low,mid-1,target)
            else:
                return trav(mid+1,high,target)
        return trav(0,len(nums)-1,target)