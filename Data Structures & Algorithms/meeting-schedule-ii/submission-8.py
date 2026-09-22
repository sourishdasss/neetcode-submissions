"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals
        intervals.sort(key = lambda x : x.start)

        heap = []
        count = 0

        if intervals:
            count += 1

        for i in intervals:
            s = i.start
            e = i.end
            
            if not heap:
                heapq.heappush(heap, e)

            else:
                # heap is not empty

                earliest = heap[0]

                if s >= earliest:
                    # start is after, so we can pop the heap and append the new start       
                    heapq.heappop(heap)
                    heapq.heappush(heap, e)

                else:
                    # we need a new room
                    heapq.heappush(heap, e)
                    count += 1

        return count