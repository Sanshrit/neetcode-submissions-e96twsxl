class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        n = numCourses
        adj = [[] for _ in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        indegree = [0 for _ in range(n)]
        for i in range(len(adj)):
            for node in adj[i]:
                indegree[node]+=1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)
            for x in adj[node]:
                indegree[x]-=1
                if indegree[x] == 0:
                    q.append(x)
        
        if len(ans) == n:
            return ans
        return []
