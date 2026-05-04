class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        print(freq)

        sorted_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        
        ans = []
        i = 0
        while i < k:
            ans.append(sorted_freq[i][0])
            i += 1

        return ans