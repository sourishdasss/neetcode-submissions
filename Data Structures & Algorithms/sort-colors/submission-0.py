class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap = []
        # for i, n in enumerate(nums):
        #     nums.pop(i)
        #     heapq.heappush(heap, n)
        #     print(nums)
        
        while nums:
            tmp = nums.pop()
            heapq.heappush(heap, tmp)

        while heap:
            tmp = heapq.heappop(heap)
            nums.append(tmp)

        

        
        