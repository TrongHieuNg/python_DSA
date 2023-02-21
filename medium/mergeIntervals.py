"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover 
all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Time complexity: O(nlogn)

Space complexity: O(1)
"""

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
    intervals.sort()
    i, j = 0, 1
    while j < len(intervals):
        if intervals[i][1] >= intervals[j][0]:
            intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[j][1])]
            intervals.pop(j)
        else:
            i += 1
            j += 1
    return intervals
