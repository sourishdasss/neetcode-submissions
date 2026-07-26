"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals
        intervals.sort(key = lambda x: x.start)

        # init min heap
        min_heap = []

        if not intervals:
            return 0
        
        heapq.heappush(min_heap, intervals[0].end)
        count = 1

        for i in range(1, len(intervals)):
            m = min_heap[0]

            print(intervals[i].start, m)
            print(min_heap)

            if intervals[i].start < m:
                heapq.heappush(min_heap, intervals[i].end)
                count += 1
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, intervals[i].end)
            

            print(min_heap)
        
        return count


