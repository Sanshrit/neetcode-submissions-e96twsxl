from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,time))
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            row,col,t = q.popleft()
            time = max(time,t)
            for i,j in dirs:
                nrow = row + i
                ncol = col + j
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    q.append((nrow,ncol,t+1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1        
        return time

        