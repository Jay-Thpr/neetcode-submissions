'''
given a rectangular island, value at index represents height at coord

can flow to neighboring call with height <= itself

find cells which can flow to (top or left) and (right or bottom)

brute force:
    - for each r, c: run bfs/dfs to see if both oceans can be seen
    - repetitive number comparisons
    - O(n*m)^2

instead:
    - set of valid cells are cells that can be flooded into (going reverse)
    - start from outside in, then return alls cells that get flooded into

algo:
    - hash set of seen indices per ocean
    - for each value at a row/column bordering either ocean:
        - bfs/dfs into neighboring cells that have not yet been seen and are >= current cell
        - when no more cells to flood into, return

    - return the indices that are found in pacific and atlantic set
        - for each index, add to result list if in both sets
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        #mark all the indices that can be flooded into
        def dfs(i, j, ocean_set, prev_height):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in ocean_set or prev_height > heights[i][j]:
                return
            
            ocean_set.add((i, j))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in directions:
                dfs(i + dr, j + dc, ocean_set, heights[i][j])
        
        #flood into indices starting from the outer rows/cols
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
            

        