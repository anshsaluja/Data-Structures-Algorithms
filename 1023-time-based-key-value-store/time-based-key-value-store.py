class TimeMap(object):

    def __init__(self):

        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        if key not in self.store:
            return ""
        
        values = self.store[key]

        
        left = 0
        right = len(values)-1
        answer = ""

        while left<=right:

            mid = (left+right)//2

            if values[mid][0]<=timestamp:
                answer = values[mid][1]
                left = mid+1
            
            else:
                right = mid-1
        return answer


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)