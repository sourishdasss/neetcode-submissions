import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # find correct row
        last_col = [matrix[i][n-1] for i in range(m)]

        row = bisect.bisect_left(last_col, target)

        print(row, m)

        if row >= m:
            return False

        # check given row
        col = bisect.bisect_left(matrix[row], target)

        print(col)

        if matrix[row][col] == target:
            return True
        else:
            return False
