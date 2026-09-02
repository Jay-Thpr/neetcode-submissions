'''
given an array of integers nums and an integer k
return the total number of subarrays whose sum equals to k

CONTIGUOUS non-empty sequence of elements within an array.

brute force: for each index, check if adding the next index iteravely sums to the target
can you use prefix sum?
    as you go through the array, collect prefix sum, store amount of previous prefix sums
    - for each prefix sum, does there previously exist some earlier prefix sum that chopping that off would result in k?


'''
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix_sum = 0
        res = 0
        prefix[0] = 1

        for n in nums:
            prefix_sum += n
            res += prefix[prefix_sum - k]
            prefix[prefix_sum] += 1

        
        return res
        