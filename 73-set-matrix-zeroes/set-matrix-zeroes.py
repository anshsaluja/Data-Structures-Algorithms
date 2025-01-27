class Solution(object):
    def setZeroes(self, matrix): 

        first_row = False
        first_col = False

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if(matrix[i][j]==0):
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        if first_row:
            for j in range(col):
                matrix[0][j] = 0

        if first_col:
            for i in range(row):
                matrix[i][0] = 0

   
    
    #     for i in range(1,row):
    #         for j in range(1,col):
    #             if(matrix[i][0]==0 or matrix[0][j]==0):
    #                 matrix[i][j]=0
        
    #     if first_row:
    #         for j in range(col):
    #             matrix[0][j]=0
        
    #     if first_col:
    #         for i in range(row):
    #             matrix[i][0]=0





       
        

      

    
        
        
        