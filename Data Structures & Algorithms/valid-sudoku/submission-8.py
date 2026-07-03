class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue

                if curr not in rows[i]:
                    rows[i].add(curr)
                else:
                    return False
                
                if curr not in cols[j]:
                    cols[j].add(curr)
                else:
                    return False
                idx = (i//3) + (j//3)*3
                if curr not in boxes[idx]:
                    boxes[idx].add(curr)
                else:
                    return False
        return True          

                



