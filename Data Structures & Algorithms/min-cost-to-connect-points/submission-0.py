class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for _ in range(len(points))]
        vis = [0 for _ in range(n)]
        def dist(x1,y1,x2,y2):
            return abs(x2-x1) + abs(y2-y1)
        
        for i in range(n):
            for j in range(i+1,n):
                if j!=i:
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    d = dist(x1,y1,x2,y2)
                    adj[i].append([j,d])
                    adj[j].append([i,d])
        
        heap = []
        heapq.heappush(heap,[0,0])
        sum = 0
        while heap:
            w,node = heapq.heappop(heap)
            if vis[node] == 0:
                vis[node] = 1
                sum+=w
                for nd, w in adj[node]:
                    if not vis[nd]:
                        heapq.heappush(heap,[w,nd])
        return sum
