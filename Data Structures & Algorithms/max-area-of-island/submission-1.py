class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(i, j):
            nonlocal max_area
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            
            max_area += 1
            grid[i][j] = 0

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
                res = max(res, max_area)
                max_area = 0
        
        return res

