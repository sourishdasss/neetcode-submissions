class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Length of 1
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True

        print(dp)

        for l in range(3, n+1):
            for i in range(n-l+1):
                # print(l, i)
                print(i, i+l-1)
                print(i+1, i+l-2)
                print(s[i] == s[i+l-1], dp[i+1][i+l-2])

                if s[i] == s[i+l-1] and dp[i+1][i+l-2]:
                    dp[i][i+l-1] = True

        print(dp)

        max_diff = 0
        bounds = (0,0)
        # find longest substring
        for i in range(n):
            for j in range(n):
                diff = j - i
                if diff >= 0 and dp[i][j]:
                    if diff > max_diff:
                        max_diff = diff
                        bounds = (i,j)
        print(bounds)

        return s[bounds[0]:bounds[1]+1]
