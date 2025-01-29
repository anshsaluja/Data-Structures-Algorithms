class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = float('-inf')
        current = 0

        for i in range(len(nums)):
            current+=nums[i]

            if current>max:
                max = current
            
            if current<0:
                current = 0
            
        return max


        