class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ans = []
        n = len(heights)
        m = len(heights[0])

        def dfs(row,col,ds):
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dirs:
                nrow = row + i
                ncol = col + j

                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and heights[row][col] <= heights[nrow][ncol] and (nrow,ncol) not in ds:
                    ds.add((nrow,ncol))
                    dfs(nrow,ncol,ds)
        
        # pacific top and bottom atlantic
        for i in range(m):
            pacific.add((0,i))
            dfs(0,i,pacific)

            atlantic.add((n-1,i))
            dfs(n-1,i,atlantic)
        # pacific left and atlantic right
        for i in range(n):
            pacific.add((i,0))
            dfs(i,0,pacific)

            atlantic.add((i,m-1))
            dfs(i,m-1,atlantic)
        
        for x in pacific:
            if x in atlantic:
                ans.append(list(x))
        return ans
                