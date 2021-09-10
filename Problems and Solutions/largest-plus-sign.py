# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. 
# The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's.
# Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

# Example 1:
  
# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        top = [[ 0 for i in range(n)] for j in range(n)]
        left = [[ 0 for i in range(n)] for j in range(n)]
        right = [[ 0 for i in range(n)] for j in range(n)]
        bottom = [[ 0 for i in range(n)] for j in range(n)]
        s = set()
        for i,j in mines:
            s.add((i,j))
        
        def fillTopLeft():
            for i in range(n):
                for j in range(n):
                    if (i,j) not in s:
                        if i==0:
                            top[i][j] = 1
                        else:
                            top[i][j] = top[i-1][j] + 1
                        if j==0:
                            left[i][j] = 1
                        else:
                            left[i][j] = left[i][j-1] + 1
        
        def fillBottomRight():
            for i in range(n-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if (i,j) not in s:
                        if i==n-1:
                            bottom[i][j] = 1
                        else:
                            bottom[i][j] = bottom[i+1][j] + 1
                        if j==n-1:
                            right[i][j] = 1
                        else:
                            right[i][j] = right[i][j+1] + 1
                            
        fillTopLeft()
        fillBottomRight()
        ans = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in s:
                    ans = max(ans, min(left[i][j], right[i][j], top[i][j], bottom[i][j]))
        return ans
