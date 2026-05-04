class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        print(heap)

        while len(heap) > 1:
            h_1 = -heapq.heappop(heap)
            h_2 = -heapq.heappop(heap)

            if h_1 != h_2:
                diff = abs(h_2 - h_1)
                heapq.heappush(heap, -diff)
            print(heap)
        
        if not heap:
            return 0
        else:
            return -heap[0]