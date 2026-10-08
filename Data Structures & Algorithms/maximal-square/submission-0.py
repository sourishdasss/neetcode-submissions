class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        print(m, n)
        
        dp = [[0] * (n+1) for _ in range(m+1)]

        maximal_side = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                print(i, j)


                # the matrix to see if it's a 1
                if matrix[i][j] == "1":
                    # check the bottom right, bottom and right
                    br = dp[i+1][j+1]
                    b = dp[i+1][j]
                    r = dp[i][j+1]

                    dp[i][j] = min(br, b, r) + 1

                    print('jhere')

                    maximal_side = max(maximal_side, dp[i][j])

        print(dp)

        return maximal_side * maximal_side
        
        