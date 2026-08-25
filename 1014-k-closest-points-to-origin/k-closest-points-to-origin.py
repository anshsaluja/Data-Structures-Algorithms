class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []

        for x, y in points:
            distance = x*x + y*y
            heap.append((distance, x, y))

        heapq.heapify(heap)


        result = []

        for i in range(k):
            distance , x , y = heapq.heappop(heap)
            result.append([x,y])

        return result
        