class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        def dfs(row,col):
            vis[row][col] = 1
            area = 1
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dirs:
                nrow = row + i
                ncol = col + j

                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] ==1 and vis[nrow][ncol]==0:
                    area+=dfs(nrow,ncol)
            return area
        
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == 1:
                    ans= max(ans,dfs(i,j))
        return ans