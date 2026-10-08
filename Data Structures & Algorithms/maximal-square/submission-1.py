class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maximal_side = 0
        
        # store max side lens as if the given point is the top-left
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # the matrix to see if it's a 1
                if matrix[i][j] == "1":
                    # check the bottom right, bottom and right
                    br = dp[i+1][j+1]
                    b = dp[i+1][j]
                    r = dp[i][j+1]

                    dp[i][j] = min(br, b, r) + 1
                    maximal_side = max(maximal_side, dp[i][j])

        return maximal_side * maximal_side
        
        