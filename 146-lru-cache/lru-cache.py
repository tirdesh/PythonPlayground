class Node:
    def __init__(self, key, val, left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru  = Node(0,0)
        self.mru = Node(0,0)
        self.lru.right = self.mru
        self.mru.left = self.lru

    def remove(self,key):
        node = self.cache[key]
        pre = node.left
        nex  = node.right
        pre.right = nex
        nex.left = pre

    def insert(self,key,value):
        node =  Node(key, value)
        temp = self.mru.left
        temp.right = node
        self.mru.left = node
        node.right = self.mru
        node.left = temp
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.remove(key)
        del self.cache[key]
        node = self.insert(key,val)
        self.cache[key] = node
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(key)
        node = self.insert(key,value)
        self.cache[key] = node
        if self.capacity < len(self.cache):
            key_to_be_deleted = self.lru.right.key
            self.remove(key_to_be_deleted)
            del self.cache[key_to_be_deleted]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)