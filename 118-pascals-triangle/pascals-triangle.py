class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []

        if numRows<=0:
            return result
    
        result = [[1]]

        if numRows<2:
            return result

        for i in range(1,numRows):
            prev = result[i-1]
            row = [1]

            for j in range(1,len(prev)):
                row.append(prev[j-1]+prev[j])
            
            row.append(1)

            result.append(row)

        return result
        
    
    
    
    