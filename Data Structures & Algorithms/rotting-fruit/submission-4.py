'''
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
    - must track the total number of fruits, and the number of rotten fruits must be equal to the number of total fruits

bfs out from each rotten fruit
    - have a queue of rotten fruit
    - for each rf in q:
        - append all fresh fruit neighbors of rf to q 
        - set all neighbors to be rotten
        - decrement fresh fruit count by count of fresh neighbors
        - pop rf from q

    - when the q is empty (no more fruit to set as raw):
        - return the num of bfs steps (or -1 if fresh fruit > 0)

'''
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = deque()
        fresh_fruit = 0
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_fruit += 1

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while q and fresh_fruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        fresh_fruit -= 1
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            res += 1

        return -1 if fresh_fruit != 0 else res
        

