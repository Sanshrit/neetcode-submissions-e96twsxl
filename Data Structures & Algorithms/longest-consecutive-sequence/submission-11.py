class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            seen.add(i)
        
        ans = 0
        for i in nums:
            t = i
            if t-1 in seen:
                continue
            count =1
            while t+1 in seen:
                count+=1
                t+=1
            ans = max(ans,count)
        return ans