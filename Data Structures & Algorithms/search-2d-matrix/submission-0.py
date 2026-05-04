class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We can use a divide and conquer algorithm 
        matrix_rows = len(matrix)

        # We can check against the end of each row
        
        tmp_row = []

        cols = len(matrix[0]) - 1

        print(cols)

        for row in matrix:
            if row[0] <= target and target <= row[cols]:
                tmp_row = row

        for i in tmp_row:
            if i == target:
                return True
            
        return False