'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
- each row 1-9 w/out duplicates
- each col 1-9 w/out duplicates
- each 3x3 subxos 1-9 w/out duplicates

initial thought:
just brute force

'''



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                box_idx = (r // 3, c // 3)

                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_idx]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
        

        