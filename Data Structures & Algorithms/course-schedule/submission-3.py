class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n+1)]
        for a,b in prerequisites:
            adj[b].append(a)
        
        indegree = [0 for _ in range(n+1)]
        for x in adj:
            for i in x:
                indegree[i]+=1
            
        q = deque()
        for i in range(n+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            for i in adj[x]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
        for i in range(n+1):
            if indegree[i] !=0:
                return False
        return True

