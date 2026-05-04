class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 0
        n = len(intervals)
        output = []

        start = intervals[i][0]
        end = intervals[i][1]
        while i < n:
            
            # take a greedy approach
            while i+1 < n and end >= intervals[i+1][0]:
                end = max(end, intervals[i+1][1])
                i += 1
            
            output.append([start, end])
            i += 1

            if i < n:
                start = intervals[i][0]
                end = intervals[i][1]
        
        return output
