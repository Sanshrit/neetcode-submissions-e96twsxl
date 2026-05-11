class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def findUlpPar(self,node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.findUlpPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self,u,v):
        ulp_u = self.findUlpPar(u)
        ulp_v = self.findUlpPar(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = self.parent[ulp_v]
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = self.parent[ulp_u]
            self.size[ulp_u] += self.size[ulp_v]            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        for u,v in edges:
            ds.unionBySize(u,v)
        ans = 0
        for i in range(n):
            if ds.findUlpPar(i) == i:
                ans+=1
        return ans

        