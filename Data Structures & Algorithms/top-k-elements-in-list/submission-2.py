class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 0 
        
        sorted_freq = sorted(freq, key=lambda x : freq[x], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_freq[i])

        return res

        