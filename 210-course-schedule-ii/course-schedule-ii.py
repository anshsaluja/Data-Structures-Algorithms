class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(numCourses)]

        for course, prereq in  prerequisites:
            graph[course].append(prereq)
        
        state = [0] * numCourses

        result = []

        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1

            for prereq in graph[course]:
                if dfs(prereq) == False:
                    return False

            state[course] = 2
            result.append(course)
            return True

        
        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return result
        