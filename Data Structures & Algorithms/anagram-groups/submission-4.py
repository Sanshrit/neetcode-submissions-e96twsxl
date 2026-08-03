class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}

        for st in strs:
            v1 = [0]*26
            for char in st:
                v1[ord(char)-ord('a')]+=1
            key = tuple(v1)
            if key in d1:
                d1[key].append(st)
            else:
                d1[key] = [st]
        
        ans = []
        for i in d1.values():
            ans.append(i)
        return ans