class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        # print(freq.items())

        sorted_freq = sorted(freq.items(), key=lambda x : x[1], reverse=True)

        # print(sorted_freq)

        output = []

        for i in range(k):
            output.append(sorted_freq[i][0])

        return output
