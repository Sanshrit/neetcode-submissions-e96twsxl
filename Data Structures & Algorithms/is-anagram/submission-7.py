class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        v1 = [0]*26
        v2 = [0]*26

        for i in range(len(s)):
            v1[ord(s[i]) - ord('a')]+=1
        for i in range(len(t)):
            v2[ord(t[i]) - ord('a')]+=1
        return v1 == v2