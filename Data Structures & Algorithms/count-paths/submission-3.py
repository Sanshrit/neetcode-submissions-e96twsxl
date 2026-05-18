class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            up,left = 0,0
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                if row > 0:
                    up = dp[row-1][col]
                if col > 0:
                    left = dp[row][col-1]
                dp[row][col] = up + left
        return dp[m-1][n-1]
            