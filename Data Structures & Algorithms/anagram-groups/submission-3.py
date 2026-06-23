class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map of a list[26]
        d1 = {}
        for word in strs:
            temp = [0]*26
            for ch in word:
                temp[ord(ch)-ord('a')]+=1
            key = tuple(temp)
            if key in d1:
                d1[key].append(word)
            else:
                d1[key] = [word]
        
        ans = []
        for x in d1.keys():
            temp = []
            for a in d1[x]:
                temp.append(a)
            ans.append(temp)
        return ans
