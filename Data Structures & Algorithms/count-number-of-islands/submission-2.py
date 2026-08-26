class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def mark(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            mark(i-1, j)
            mark(i+1, j)
            mark(i, j-1)
            mark(i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    mark(i, j)

        return islands

        