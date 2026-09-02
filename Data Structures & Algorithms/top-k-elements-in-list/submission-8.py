'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

answer is always unique.

You may return the output in any order.

need to track: frequency
- for each num, use hashmap to map the count of that num

- once hashmap is created, can use a minheap to store k items

- if the item frequency is less than the min stored item frequency, skip

time complexity O(nlogk) - 2 n time loops, heap logk
space complexity O(n + k) -> O(n)


instead of this, can track frequency in a list and work backwords
    - have a list of lists of nums that have a specific frequency, work backwords from that frequency count list



'''

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for n in nums:
            d[n] = 1 + d.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in d.items():
            freq[count].append(num)
            
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if k == len(res):
                    return res
        


