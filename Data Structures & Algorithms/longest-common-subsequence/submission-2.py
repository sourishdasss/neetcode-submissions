class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # n1 = len(text1)
        # n2 = len(text2)
        
        # dp = [[0 for _ in range(n2)] for _ in range(n1)]

        # # populate first row
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1

        # for i in range(1, n2):
        #     dp[0][i] = dp[0][i-1] 
        #     if text1[0] == text2[i]:
        #         dp[0][i] = 1

        # for i in range(1, n1):
        #     for j in range(n2):
        #         # check directly above and left 
        #         if j == 0:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        #         # check if letters match
        #         if text1[i] == text2[j]:
        #             dp[i][j] += 1
        
        # print(dp)

        # return dp[-1][-1]

        n1, n2 = len(text1), len(text2)
        dp = [[0] * n2 for _ in range(n1)]

        # first cell
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        # first row
        for j in range(1, n2):
            dp[0][j] = dp[0][j-1]
            if text1[0] == text2[j]:
                dp[0][j] = 1

        # first col
        for i in range(1, n1):
            dp[i][0] = dp[i-1][0]
            if text1[i] == text2[0]:
                dp[i][0] = 1

        # rest
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]