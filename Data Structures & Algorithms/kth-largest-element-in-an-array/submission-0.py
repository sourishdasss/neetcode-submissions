import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create max heap
        max_heap = []
        for num in nums:
            tmp = -1 * num
            heapq.heappush(max_heap, tmp)

        # look for kth largest element
        answer = 0
        for i in range(k):
            answer = -heapq.heappop(max_heap)

        return answer