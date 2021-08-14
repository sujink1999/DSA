# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
                
        for j in cols:
            for i in range(len(matrix)):
                if i not in rows:
                    matrix[i][j] = 0
