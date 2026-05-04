class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # init dp table
        # j -> amount (starting with 0)
        # i -> set of coins we can use

        coins.sort(reverse=True)
        print(coins)

        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for row in dp:
            row[0] = 1


        # try with one coin
        for j in range(1, amount+1):
            diff = j - coins[0]
            if diff > -1 and diff < (amount + 1):
                dp[0][j] = dp[0][diff]
        

        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                diff = j - coins[i]
                if diff > -1 and diff < (amount + 1):
                    dp[i][j] += dp[i][diff]
                dp[i][j] += dp[i-1][j]
        
        print(dp)
        return dp[-1][-1]
