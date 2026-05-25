class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        set1 = set()
        for word in words:
            for ch in word:
                set1.add(ch)
        
        n = len(set1)
        idx = {ch:i for i,ch in enumerate(set1)}
        rev = {i:ch for i,ch in enumerate(set1)}
        adj = [[] for _ in range(n)]
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1),len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[idx[w1[j]]].append(idx[w2[j]])
                    break
        
        def topSort(adj):
            indegree = [0 for _ in range(n)]
            ans = []
            for x in adj:
                for i in x:
                    indegree[i]+=1
            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                node = q.popleft()
                ans.append(node)
                for x in adj[node]:
                    indegree[x]-=1
                    if indegree[x]==0:
                        q.append(x)
            if len(ans) == n:
                return ans
            return []
        
        ans = topSort(adj)
        s = ""
        for x in ans:
            s += rev[x]
        return s


