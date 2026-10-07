"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        
        min_heap = []
        size = 0

        for i in intervals:
            s, e = i.start, i.end

            # for empty heap
            if not min_heap:
                heapq.heappush(min_heap, e)
                size += 1
            elif s < min_heap[0]:
                heapq.heappush(min_heap, e)
                size += 1
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, e)

        return size