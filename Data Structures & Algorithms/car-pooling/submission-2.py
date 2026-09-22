class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort trips by closest start
        trips.sort(key = lambda x : x[1])

        heap = []
        curr_capacity = capacity
        
        for n, s, e in trips:

            # first trip
            if not heap:
                if n <= curr_capacity:
                    heapq.heappush(heap, [e, n])
                    curr_capacity -= n
                else:
                    return False
            
            else:
                # remove passengers that are reaching their destinations
                while heap and heap[0][0] <= s:
                    curr_capacity += heap[0][1]
                    heapq.heappop(heap)
                
                # add new passengers
                heapq.heappush(heap, [e, n])
                curr_capacity -= n
                
                if curr_capacity < 0:
                    return False
            
        return True


            