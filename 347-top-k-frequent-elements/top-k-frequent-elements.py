class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        map = {}

        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
        

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])

        for num in map:
            value = map[num]
            bucket[value].append(num)

        result = []
        i = len(nums)

        while i>0:
            for num in bucket[i]:
                result.append(num)

                if len(result)==k:
                    return result
            i-=1

        