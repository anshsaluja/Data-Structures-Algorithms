class Solution(object):
    def setZeroes(self, matrix):     
        first_row = False
        first_col = False

        rows = len(matrix)
        cols = len(matrix[0])

        # 1) Identify rows & columns that need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 2) Zero out the inner cells using the flags in first row & column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 3) If the first row should be zero, set all columns in row 0 to zero
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        # 4) If the first column should be zero, set all rows in column 0 to zero
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
        
        