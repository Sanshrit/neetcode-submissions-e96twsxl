from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        dist = 0
        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            row,col,d = q.popleft()
            for i,j in dirs:
                nrow = row+i
                ncol = col+j

                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == 2147483647 and visited[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    grid[nrow][ncol] = d+1
                    q.append((nrow,ncol,d+1))