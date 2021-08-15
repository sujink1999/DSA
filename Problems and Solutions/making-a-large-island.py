
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dis = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i, j, it):
            grid[i][j] = it
            area = 1
            for di in dis:
                ni = i + di[0]
                nj = j + di[1]
                if (ni > -1 and ni < len(grid)) and (nj>-1 and nj < len(grid[0])) and grid[ni][nj] == 1:
                    area += dfs(ni, nj, it)
            return area
        
        waters = []
        it = 2
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    waters.append([i,j])
                else:
                    if grid[i][j] == 1:
                        d[it] = dfs(i,j,it)
                        it+=1
        ans = 0 if len(d.values())==0 else max(d.values())
        for water in waters:
            i = water[0]
            j = water[1]
            s = set()
            for di in dis:
                ni = i + di[0]
                nj = j + di[1]
                if (ni > -1 and ni < len(grid)) and (nj>-1 and nj < len(grid[0])) and grid[ni][nj] != 0:
                    s.add(grid[ni][nj])
            total = 1
            for k in s:
                total+=d[k]
            ans = max(ans, total)
        return ans
