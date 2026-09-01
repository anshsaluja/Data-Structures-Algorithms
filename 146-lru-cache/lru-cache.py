class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # hashmap
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right # connecting the nodes, left -> right
        self.right.prev = self.left # connecting the nodes, right -> left
    
    def remove(self, node):
        prev_node = node.prev   # suppose A,B,C are connected doubly, prev_node = A
        next_node = node.next   # next_node = C

        prev_node.next = next_node # A->C
        next_node.prev = prev_node # C->A

        # removes B

    def insert(self,node):
        prev_node = self.right.prev # suppose we want to insert C, so B, right in doubly
        # this stores B

        prev_node.next = node # B->C
        node.prev = prev_node # C->B

        node.next = self.right # C->right
        self.right.prev = node # right->C

        # inserts C

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)