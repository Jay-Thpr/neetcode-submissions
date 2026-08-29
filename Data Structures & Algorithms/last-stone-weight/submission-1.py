import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]

        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x == y:
                continue
            heapq.heappush(heap, y-x)
        
        if heap:
            return -heap[0]
        return 0