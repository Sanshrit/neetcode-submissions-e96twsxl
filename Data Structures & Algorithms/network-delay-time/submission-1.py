class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,wt in times:
            adj[u].append([v,wt])
        ans = -1
        dist = [1e6 for _ in range(n+1)]
        dist[k]=0
        pq = []
        heapq.heappush(pq,[0,k])
        while pq:
            d,nd = heapq.heappop(pq)
            for node,di in adj[nd]:
                if d + di < dist[node]:
                    dist[node] = d+di
                    heapq.heappush(pq,[d+di,node])
        
        for i in range(1,n+1):
            if dist[i]==1e6:
                return -1
            ans = max(ans,dist[i])
        return ans
