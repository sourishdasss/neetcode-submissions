class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort()

        print(intervals)

        count = 0

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            tmp_start = intervals[i][0]
            tmp_end = intervals[i][1]

            if tmp_start < end:
                count += 1

                print([tmp_start, tmp_end])

                
                end = min(end, tmp_end)

            
            else:
                start = tmp_start
                end = tmp_end
        
        return count
