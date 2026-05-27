class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def isSafe(row,col):
            #upper diag
            rrow = row
            ccol = col

            while rrow>=0 and ccol>=0:
                if board[rrow][ccol] == 'Q':
                    return False
                rrow-=1
                ccol-=1

            rrow = row
            ccol = col                
            # same row left
            while ccol>=0:
                if board[rrow][ccol] == 'Q':
                    return False
                ccol-=1

            #bottom left diag                
            rrow = row
            ccol = col

            while rrow < n and ccol>=0:
                if board[rrow][ccol] == 'Q':
                    return False
                rrow+=1
                ccol-=1
            return True

        

        def solve(col):
            if col == n:
                ans.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                if isSafe(row,col):
                    board[row][col] ='Q'
                    solve(col+1)
                    board[row][col] = '.'
        solve(0)                    
        return ans