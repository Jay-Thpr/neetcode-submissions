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

        ROW, COL = len(board), len(board[0])

        seen = set()

        for r in range(ROW):
            seen = set()
            for c in range(COL):
                if board[r][c].isdigit() and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for c in range(COL):
            seen = set()
            for r in range(ROW):
                if board[r][c].isdigit() and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for i in range(3):
            for j in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        temp_r = i * 3 + r
                        temp_c = j * 3 + c
                        if board[temp_r][temp_c].isdigit() and board[temp_r][temp_c] in seen:
                            return False
                        seen.add(board[temp_r][temp_c])

        return True
        

        