"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        seen = {}

        def dfs(cur):
            if cur in seen:
                return seen[cur]
            
            copy = Node(cur.val)
            seen[cur] = copy

            for n in cur.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy

        return dfs(node)