'''
intuition:
    - prims

'''


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        res = 0
        visit = set()
        heap = [[0, 0]] #[cost, point index]

        while len(visit) < n:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_c, nei_i in adj[i]:
                if nei_i not in visit:
                    heapq.heappush(heap, [nei_c, nei_i])
        
        return res


