"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        
        visited = {}

        def dfs(cur):
            if cur in visited:
                return visited[cur]

            clone = Node(cur.val)
            visited[cur] = clone

            for neighbor in cur.neighbors:
                cloned_neighbor = dfs(neighbor)
                clone.neighbors.append(cloned_neighbor)

            return clone
        return dfs(node)
        