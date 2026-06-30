class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i,j,0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            row,col,dist = q.popleft()
            for i,j in dirs:
                nrow = row + i
                ncol = col + j
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == 2147483647:
                    grid[nrow][ncol] = dist + 1
                    q.append([nrow,ncol,dist+1])

