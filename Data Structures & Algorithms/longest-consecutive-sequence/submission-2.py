class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store a set of previous elements in each cell
        curr_nums = set(nums)
        ans = [1] * len(nums)


        for i, n in enumerate(nums):
            # check if prev is in curr_nums set
            tmp = n

            if tmp - 1 not in curr_nums:
                length = 1

                while tmp + length in curr_nums:
                    ans[i] += 1
                    length += 1
        
        if ans:
            return max(ans)
        else:
            return 0
            