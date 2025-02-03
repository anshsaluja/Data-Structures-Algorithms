class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(intervals)<=1:
            return intervals
        

        intervals.sort()
        
        result = []
        new_interval = intervals[0]
        result.append(new_interval)


        for i in range(1,len(intervals)):
            if intervals[i][0] <= new_interval[1]:
                new_interval[1] = max(intervals[i][1], new_interval[1])
            else:
                new_interval = intervals[i]
                result.append(new_interval)
        
        return result
            





        
        # if len(intervals)<=1:
        #     return intervals

        
        # intervals.sort()

        # result = []
        # new_interval = intervals[0]
        # result.append(new_interval)

        # for i in range(1,len(intervals)):
        #     if intervals[i][0]<=new_interval[1]:
        #         new_interval[1] = max(new_interval[1], intervals[i][1])
        #     else:
        #         new_interval = intervals[i]
        #         result.append(new_interval)
        
        # return result

        