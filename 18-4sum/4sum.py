class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                    continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k<l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]

                    if sum == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)

                        k+=1
                        l-=1

                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                    
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    
                    elif sum<target:
                        k+=1
                
                    else:
                        l-=1
        return ans
        