class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(row,col):
            vis[row][col] = 1
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dirs:
                nrow = row + i
                ncol = col + j
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == '1':
                    dfs(nrow,ncol)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    ans+=1
                    dfs(i,j)
        return ans