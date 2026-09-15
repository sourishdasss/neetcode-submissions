class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        cutoff = size // 2
        dic = defaultdict(int)
        
        for n in nums:
            dic[n] += 1

            if dic[n] > cutoff:
                return n

        return 0
