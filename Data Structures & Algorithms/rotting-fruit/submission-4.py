class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
        time = 0
        while q:
            row,col,t = q.popleft()
            time = max(time,t)
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for i,j in dirs:
                nrow = row + i
                ncol = col + j
            
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == 1 and vis[nrow][ncol] == 0:
                    vis[nrow][ncol] = 1
                    grid[nrow][ncol] = 2
                    q.append([nrow,ncol,t+1])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return time

