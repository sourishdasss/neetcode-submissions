class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # determine frequencies of each number in the array
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # sort by frequency
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        elements = []
        for key in freq:
            elements.append(key)
        
        return elements[:k]
