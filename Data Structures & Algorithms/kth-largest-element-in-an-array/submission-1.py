class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        tmp = 0
        ans = -1

        for n in nums:
            heapq.heappush(heap, -n)

        while tmp < k:
            ans = -heapq.heappop(heap)
            tmp += 1
        
        return ans