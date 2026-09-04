'''
given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day

brute force:
- for each index, traverse right until larger number is found or end of the array
    - O(n^2)
- observation: days with unresolved warmer temperatures naturally decrease in falue
- if today is warmer than previous day, then today is its next warmer day
    - taking this approach, we can continue if we find a warmer day, then work backwords until it is no locker a warmer day

naturally: stack
- maintain a decreasing stack - if a warmer day is found, we set the output of the colder index to be the difference between the warm day and the cold day
    - naturally, we store indices in the stack
- whil current temp > temp at the top of the stack, pop index and calc distance
- push current index onto the stack

O(n) time, since each value is computed twice at most, O(n) space since stack can be max O(n)
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res
                
        