class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = float('-inf')
        for x in piles:
            high = max(high,x)
        
        ans = 0
        def canEat(speed):
            temp_h = h
            for x in piles:
                temp_h -= math.ceil(x/speed)
            if temp_h>=0:
                return True
            return False
        while low<=high:
            mid = (low + high)//2
            if canEat(mid) == True:
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans