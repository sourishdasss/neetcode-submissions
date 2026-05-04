class KthLargest:
    k: int
    heap: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # make a copy
        copy = []
        for num in self.heap:
            copy.append(num)
        # find k-th largest num
        end = len(copy) - self.k + 1
        for i in range(end):
            ans = heapq.heappop(copy)

        return ans
