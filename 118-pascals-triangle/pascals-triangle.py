class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []

        if numRows<=0:
            return result
        

        first_row = [1]
        result.append(first_row)

        if numRows<2:
            return result

        
        for i in range(1,numRows):
            prev_row = result[i-1]

            row = [1]

            for j in range(1,len(prev_row)):
                row.append(prev_row[j-1] + prev_row[j])
            

            row.append(1)

            result.append(row)


        return result
         

        







        # result = []

        # if numRows == 0:
        #     return result
        
        # first_row = [1]
        # result.append(first_row)

        # if numRows == 1:
        #     return result
        
        # for i in range(1,numRows):
        #     prev_row = result[i-1]

        #     row = [1]

        #     for j in range(1,len(prev_row)):
        #         row.append(prev_row[j-1] + prev_row[j])
        #     row.append(1)

        #     result.append(row)

        # return result

        
        