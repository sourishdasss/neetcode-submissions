class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = []
        max_sum.append(nums[0])

        for i in range(1, len(nums)):
            curr = max(max_sum[i-1] + nums[i], nums[i])
            max_sum.append(curr)
        
        ans = max_sum[0]
        for m in max_sum:
            ans = max(m, ans)
        
        return ans