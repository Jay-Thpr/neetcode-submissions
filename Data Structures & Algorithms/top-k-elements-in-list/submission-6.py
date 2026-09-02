'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

answer is always unique.

You may return the output in any order.

need to track: frequency
- for each num, use hashmap to map the count of that num

- once hashmap is created, can use a minheap to store k items

- if the item frequency is less than the min stored item frequency, skip

time complexity O(n) - 2 n time loops
space complexity O(n + k) -> O(n)

'''

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        min_heap = []

        for key, count in d.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, key))
            
            elif count > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (count, key))
        
        return [key for count, key in min_heap]
        


