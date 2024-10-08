""" 
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
"""
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, grid):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(i + x, j + y, grid)
        
        def is_connected():
            count = 0
            temp_grid = [row[:] for row in grid]
            for i in range(m):
                for j in range(n):
                    if temp_grid[i][j] == 1:
                        count += 1
                        if count > 1:
                            return False
                        dfs(i, j, temp_grid)
            return count == 1
        
        # Initial check if already disconnected
        if not is_connected():
            return 0
        
        # Try removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected():
                        return 1
                    grid[i][j] = 1
        
        # If grid is still connected after removing any one cell, it must take 2 removals
        return 2
