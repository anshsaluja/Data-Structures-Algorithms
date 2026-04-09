class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}

        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for num in hash: 
            count = hash[num]
            bucket[count].append(num)

        i = len(nums)
        result = []

        while i>0:
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
            i-=1
        
        