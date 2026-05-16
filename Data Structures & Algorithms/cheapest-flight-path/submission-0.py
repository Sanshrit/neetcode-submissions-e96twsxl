class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque() # (stops,node,dist)
        adj = [[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append([v,w])
        cost = [float('inf') for _ in range(n)]
        q.append((0,src,0))
        while q:
            stops,nd,dist = q.popleft()
            for dest,cst in adj[nd]:
                if dist + cst < cost[dest] and stops <=k:
                    cost[dest] = dist + cst
                    q.append((stops+1,dest,dist + cst))

        if cost[dst] != float('inf'):
            return cost[dst]
        return -1
