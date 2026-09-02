'''
Given an array of intervals where intervals[i] = [start_i, end_i]
merge all overlapping intervals

return an array of the non-overlapping intervals that cover all the intervals in the input.

- if intervals are processed in sorted order by start time, then each additional interval only overlaps if it overlaps with the last processed interval

pseudocode:
sort intervals by start time
keep track of the last merged interval
if the current interval overlaps with it, merge them (take the smallest start and largest end)
otherwise, continue and treat this as the next interval

'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for start, end in intervals:
            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])
        
        return res
            

