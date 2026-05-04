class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # len 1 palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        # len 2 palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
            
        # len 3+ palindromes
        for length in range(2, n):
            for i in range(n):
                j = i + length

                if j < n:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1


        for row in dp:
            print(row)

        return count
