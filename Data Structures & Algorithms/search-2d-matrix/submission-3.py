class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def bs(data):
            l = 0
            r = len(data)-1
            while l<=r:
                mid = (l+r)//2
                if data[mid] == target:
                    return True
                elif data[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return False    


        for i in range(n):
            if matrix[i][0] <= target and matrix[i][m-1] >= target:
                return bs(matrix[i])
        return False