class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        majority1 = float('-inf')
        majority2 = float('-inf')
        votes1 = 0
        votes2 = 0
        n = len(nums)

        for i in range(len(nums)):
            if votes1 == 0 and majority2!=nums[i]:
                votes1+=1
                majority1 = nums[i]
            elif votes2 == 0 and majority1!=nums[i]:
                votes2+=1
                majority2 = nums[i]
            elif majority1 == nums[i]:
                votes1+=1
            elif majority2 == nums[i]:
                votes2+=1
            else:
                votes1-=1
                votes2-=1
        

        votes1 = 0
        votes2 = 0
        result = []
        for i in range(len(nums)):
            if majority1 == nums[i]:
                votes1+=1
            if majority2 == nums[i]:
                votes2+=1
        
        mini = (n/3)+1
        if votes1>=mini:
            result.append(majority1)
        if votes2>=mini:
            result.append(majority2)

        
        return result

        