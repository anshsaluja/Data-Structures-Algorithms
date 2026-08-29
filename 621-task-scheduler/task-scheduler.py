class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """


        count = {}

        for letter in tasks:
            if letter not in count:
                count[letter] = 0
            count[letter]+=1
        
        max_heap = []

        for letter in count:
            heapq.heappush(max_heap, -count[letter])

        queue = deque()
        time = 0


        while max_heap or queue:
            time+=1

            if max_heap:
                freq =heapq.heappop(max_heap)
                freq+=1

                if freq!=0:
                    queue.append((freq, time +n ))

            if queue and queue[0][1] == time:
                frequency, timeperiod = queue.popleft()
                heapq.heappush(max_heap, frequency)
        
        return time



        