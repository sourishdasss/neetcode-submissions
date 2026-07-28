class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        print(freq)

        max_heap = []

        for n, f in freq.items():
            heapq.heappush(max_heap, (-f, n))

        ans = []

        for i in range(k):
            tmp = heapq.heappop(max_heap)

            print(tmp)
            ans.append(tmp[1])

        return ans
