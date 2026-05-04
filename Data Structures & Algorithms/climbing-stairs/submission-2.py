class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp[1] = 1
        dp[2] = 2

        i = 3
        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        
        return dp[n]