class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make max-heap
        heap = []

        for p in points:
            x, y = p[0], p[1]
            print(x, y)
            ecd = -math.sqrt(x**2 + y**2)

            print(ecd)

            print(-math.sqrt(2))

            heapq.heappush(heap, (ecd, p))

            # check if heap size is beyond k
            if len(heap) > k:
                print(heap[0])
                heapq.heappop(heap)
        
        print(heap)
        ans = []
        for h in heap:
            ans.append(h[1])

        return ans 



