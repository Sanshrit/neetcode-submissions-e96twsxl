class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def updateRow(row):
            for i in range(0,len(matrix[0])):
                matrix[row][i] = 0
        def updateCol(col):
            for i in range(0,len(matrix)):
                matrix[i][col] = 0
                                
        rows = set()
        cols = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            updateRow(row)
        for col in cols:
            updateCol(col)        
        