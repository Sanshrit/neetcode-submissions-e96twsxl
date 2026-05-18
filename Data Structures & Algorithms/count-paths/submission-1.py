class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def f(row,col):
            if row == 0 and col == 0:
                return 1
            if row < 0 or col < 0:
                return 0
            if dp[row][col] !=-1:
                return dp[row][col]
            up = f(row-1,col)
            left = f(row,col-1)
            dp[row][col] = up+left
            return up + left
        return f(m-1,n-1)