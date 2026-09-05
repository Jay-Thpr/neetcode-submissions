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
            seen.add(a)
            seen.add(b)
        
        def dfs(a):
            nonlocal adj

            while adj[a]:
                b = adj[a][-1]
                adj[a].pop()
                dfs(b)
        res = 0

        for i in range(n):
            if i not in seen:
                res += 1
                continue
            if adj[i]:
                res += 1
                dfs(i)
        return res
            

            


