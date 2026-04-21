class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l,r=0,0
        seen = set()
        n = len(s)
        while r < n:
            if s[r] in seen:
                while s[r] in seen and l<r:
                    seen.remove(s[l])
                    l+=1
            else:
                seen.add(s[r])
                ans = max(ans,r-l+1)
                r+=1
        return ans

        