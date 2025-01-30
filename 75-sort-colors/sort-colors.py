class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        start = 0
        mid = 0
        end = len(nums)-1

        while mid<=end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums [start]
                start+=1
                mid+=1
            
            elif nums[mid] == 1:
                mid+=1
            
            else:
                nums[mid], nums[end] = nums[end] , nums[mid]
                end-=1

        