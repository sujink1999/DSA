# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(board, empty, rows, cols, boxes):
            if not empty: return True
            r, c = empty[-1]
            for k in set("123456789") - (rows[r]|cols[c]|boxes[3*(r//3)+c//3]):
                board[r][c] = k
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(k)
                if dfs(board, empty[:-1], rows, cols, boxes): return True
                board[r][c] = '.'
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.remove(k)

            return False
        
        cols, rows, boxes, empty = defaultdict(set), defaultdict(set), defaultdict(set), []
        for r, c in product(range(9), range(9)):
            if board[r][c] == ".":
                empty.append((r,c))
            else:
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(board[r][c])
        return dfs(board, empty, rows, cols, boxes)
