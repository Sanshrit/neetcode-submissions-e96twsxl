class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = ""
        def expand(s,l,r):
            res = ""
            resLen = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                resLen = max(resLen,r-l+1)
                res = s[l:r+1]
                l-=1
                r+=1
            return res,resLen
        for i in range(len(s)):
            #odd
            s1,l1 = expand(s,i,i)
            #even
            s2,l2 = expand(s,i,i+1)

            if l1 > l2:
                if len(final) < l1:
                    final = s1
            else:
                if len(final) < l2:
                    final = s2

        return final