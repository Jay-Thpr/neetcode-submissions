'''
undirected graph
given int n, array indicating the edges

initial impressions:
    - adjacency list
        - dfs into one list, treat that as 1 connected component


'''


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #initialize adjacency list

        adj = [[] for _ in range(n)]

        seen = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)
        return res
            

            


