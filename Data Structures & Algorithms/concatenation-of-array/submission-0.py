class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        curr = 0
        n = len(nums)
        ans = nums
        for i in range(n):
            ans.append(nums[i])
        return ans
        