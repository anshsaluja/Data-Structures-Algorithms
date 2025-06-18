class Solution(object):
    def setZeroes(self, matrix): 

        row = len(matrix)
        col = len(matrix[0])

        f_row = False
        f_col = False

        for i in range(row):
            for j in range(col):
                if matrix[i][j] ==0:
                    if i == 0:
                        f_row = True
                    if j == 0:
                        f_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] =0
        
        if(f_row):
            for j in range(col):
                matrix[0][j] =0
        
        if(f_col):
            for i in range(row):
                matrix[i][0] = 0


                
    



        
        





       
        

      

    
        
        
        