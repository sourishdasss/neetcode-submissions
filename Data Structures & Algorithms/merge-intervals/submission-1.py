class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        n = len(intervals)
        output = []

        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            while i+1 < n and end >= intervals[i+1][0]:
                i += 1
                end = max(end, intervals[i][1])

            output.append([start, end])
            i += 1
        
        return output

            