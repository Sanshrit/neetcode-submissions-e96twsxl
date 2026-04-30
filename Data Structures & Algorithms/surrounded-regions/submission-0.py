class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # no zero from borders can form a closed region.
        # dfs from all 0's on the edges and we mark them visited.
        # a dfs for the ramining non-visited 0's are all enclosed
        n = len(board)
        m = len(board[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        def dfs(visited,row,col):
            visited[row][col] = 1
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for i,j in dirs:
                nrow = row+i
                ncol = col+j
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and board[nrow][ncol] == 'O' and visited[nrow][ncol] == 0:
                    dfs(visited,nrow,ncol)

        #top and bottom row
        for i in range(m):
            if board[0][i] == 'O':
                dfs(visited,0,i)
            if board[n-1][i] == 'O':
                dfs(visited,n-1,i)
        
        #left and right most columns
        for i in range(n):
            if board[i][0] == 'O':
                dfs(visited,i,0)
            if board[i][m-1] == 'O':
                dfs(visited,i,m-1)
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    board[i][j] = 'X'
            






