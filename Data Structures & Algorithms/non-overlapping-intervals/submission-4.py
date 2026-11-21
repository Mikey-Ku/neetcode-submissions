class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0

        intervals.sort(key=lambda interval:  interval[0])
        if len(intervals) <= 1:
            return removals

        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removals

