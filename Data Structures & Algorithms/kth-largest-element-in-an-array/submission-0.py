'''
use a minheap of size k to track the k largest elements


'''
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            
            elif heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
            
        return heap[0]
        