import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        max_cols = [matrix[i][n-1] for i in range(m)]
        
        r = bisect.bisect_left(max_cols, target)

        if r >= m:
            return False

        c = bisect.bisect_left(matrix[r], target)

        if c >= n:
            return False

        print(matrix[r][c])

        if matrix[r][c] == target:
            return True
        
        return False

        

        