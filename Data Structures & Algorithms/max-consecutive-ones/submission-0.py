class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0

        for n in nums:
            if n == 1:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        
        max_len = max(max_len, curr_len)
        return max_len