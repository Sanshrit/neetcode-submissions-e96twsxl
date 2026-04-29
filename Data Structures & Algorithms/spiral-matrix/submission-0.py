class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        top = 0
        bottom = n-1
        left = 0
        right = m-1

        while top <= bottom and left <= right:
            # top row
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            # right column
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            #bottom row
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
                
            #left column
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans

