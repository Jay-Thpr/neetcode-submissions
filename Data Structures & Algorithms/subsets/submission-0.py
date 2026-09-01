'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets

You may return the solution in any order.

[1,2,3] --> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

travel left -> right. for each value we can either choose to keep or not keep

base case: no remaining values. simply return nothing and append the existing list onto the result list

run dfs on each index, appending to the local result list. in dfs go through case where we keep i or discard i. at the end of the dfs call we pop the value we have just appended, cleaning up the call as we go through it.


'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
            
            

