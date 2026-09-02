'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed

A consecutive sequence is a sequence of elements in which 
each element is exactly 1 greater than the previous element.

The elements do not have to be consecutive in the original array.

O(n) time.
    - can't simply sort and then go through

idea:
    to one-pass it, we must impose some condition that makes each index only be traveresed once
    - only traverse forward if the num is the first item of a sequence, otherwise skip
        - this means for each num, they're either going forward n times or being skipped, which is O(n) or 0. this is done O(n) times, so the time complexity is O(n) not O(n^2)

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 1

        for num in numSet:
            if num - 1 not in numSet:
                #it is the start of the sequence
                length = 1
                while num + length in numSet:
                    length += 1
                    longest = max(length, longest)

        return longest
        