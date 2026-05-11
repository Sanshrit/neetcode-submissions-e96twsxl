class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = [0 for _ in range(n)]

        def dfs(node,parent):
            vis[node] = 1
    
            for nd in adj[node]:
                if not vis[nd]:
                    if dfs(nd,node) == True:
                        return True
                elif nd != parent:
                    return True
            return False
    
        if dfs(0,-1) == True:
                return False
        for x in vis:
            if x == 0:
                return False
        return True