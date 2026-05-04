class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                print("i", i, "c", c)

                tmp = i - c

                if tmp < 0:
                    continue
                elif tmp == 0:
                    dp[i] = 1
                
                dp[i] = min(dp[i], dp[tmp] + 1)

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
            