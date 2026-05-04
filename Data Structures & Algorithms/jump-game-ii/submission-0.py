class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [101] * n
        dp[0] = 0

        for i in range(n):
            jump = nums[i]
            for j in range(1, jump+1):
                if j >= n or (i + j >= n):
                    break

                dp[i+j] = min(dp[i+j], dp[i] + 1)
        
        print(dp)
        return dp[-1]