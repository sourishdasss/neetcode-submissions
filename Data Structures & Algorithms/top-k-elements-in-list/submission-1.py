class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            if n in freq:
                freq[n] += 1
        
        freq_tuples = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        k_freq_elements = [item[0] for item in freq_tuples[:k]]

        return k_freq_elements