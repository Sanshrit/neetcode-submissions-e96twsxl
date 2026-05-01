class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        curr = 0
        n = len(board)
        m = len(board[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(row,col,visited,c):
            visited[row][col] = 1
            if c == len(word):
                return True
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dirs:
                nrow = row + i
                ncol = col + j
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and board[nrow][ncol] == word[c] and visited[nrow][ncol] ==0:
                    if dfs(nrow,ncol,visited,c+1):
                        return True
            visited[row][col] = 0
        

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i,j,visited,curr+1) == True:
                        return True
        return False