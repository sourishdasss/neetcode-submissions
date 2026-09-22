class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort them first
        intervals.sort()
        
        i = 0

        output = []

        n = len(intervals)

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            # run greedy approach
            while i < n - 1 and end >= intervals[i+1][0]:
                end = max(end, intervals[i+1][1])
                i += 1


            # append interval
            tmp = [start, end]
            output.append(tmp)

            i += 1
        
        return output