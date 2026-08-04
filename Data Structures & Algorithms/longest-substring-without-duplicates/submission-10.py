class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r=0
        ans=0
        seen =set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                ans = max(ans,r-l+1)
                r+=1
                
            else:
                while s[r] in seen and l<r:
                    seen.remove(s[l])
                    l+=1
        return ans