class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        if not matrix or not matrix[0]:
            return False
    
        row = len(matrix)
        col = len(matrix[0])

        position = -1

        for i in range(row):
            if matrix[i][0]<=target<=matrix[i][col-1]:
                position = i
                break

        if position == -1:
            return False
        
        left = 0
        right = col-1

        while left<=right:
            mid = left + (right-left)//2
            if matrix[position][mid] == target:
                return True
            elif matrix[position][mid]<target:
                left = mid+1
            else:
                right = mid -1
        

        return False

       