"""
given an array of distinct integers nums and a target integer target

return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

intuition for not reusing -> start from the left index and work right. once we finish using all of a number we never use it again? does this work in practice
    - [2, 3, 4] -> 6
        -Use 2: 2 2 2, 2 4. use 3: nothing. use 4: nothing
    - BUT what if [2, 3, 4] -> 8
        -Use 2: 2222, 224, 233. use 3: nothing. use 4: 44 - looks like it works

SO: we work left -> right, dfs on each index and backtrack for all potential solutions

base case:
if index is out of range return
if cur sum is > target return
if cur sum == target append to result and return

otherwise:
dfs with current index and next index

"""



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res = []
        cur_sum = 0
        cur_list = []

        def dfs(i):
            nonlocal cur_sum
            if i >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur_list.copy())
                return
            
            cur_list.append(nums[i])
            cur_sum += nums[i]

            dfs(i)

            cur_list.pop()
            cur_sum -= nums[i]
            dfs(i+1)

        dfs(0)
        
        return res

        