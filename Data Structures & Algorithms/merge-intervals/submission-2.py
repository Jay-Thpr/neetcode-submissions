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
        last_index = 0
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start <= prev_end:
                res[last_index][1] = max(prev_end, end)
                prev_end = max(prev_end, end)
            else:
                last_index += 1
                prev_start = start
                prev_end = end
                res.append([prev_start, prev_end])
        
        return res
            

