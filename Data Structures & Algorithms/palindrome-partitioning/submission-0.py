class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        ans = []
        n = len(s)
        def isPal(text,st,en):
            while st<=en:
                if text[st]!=text[en]:
                    return False
                st+=1
                en-=1
            return True
        def f(s,idx):
            if idx == n:
                ans.append(curr.copy())
                return
            
            for i in range(idx,n):
                if isPal(s,idx,i):
                    curr.append(s[idx:i+1])
                    f(s,i+1)
                    curr.pop()
        
        f(s,0)
        return ans
        