class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = Counter(nums)
        sorted_freq = sorted(count, key=lambda x : count[x], reverse=True)

        for i in range(k):
            print(sorted_freq[i])
            output.append(sorted_freq[i])

        return output
