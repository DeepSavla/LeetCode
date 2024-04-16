#we create hashmap to add and retrieve values in O(1) time. But the issue arises when we want to get the least recently used to delete when capacity is reached. we can do this with list but that will take O(n) time. Hence we are using double linked list so deleting a node once found is O(1). In order to find the node in O(1) we save the address of node in hashmap value against the key. The list also needs key, value for each node since when least recently node is deleted, we have to delete that key from hashmap too.
#eg structure:-  hashmap = {key : NodeAddress}       ;  LL = Node(key, value)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):     
        self.cap = capacity
        self.hm = {}                #cache
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail      #head is least recently used
        self.tail.prev = self.head      #tail is most recently used
    
    def remove(self, node):   #remove a node ; required to remove head(least recently used) node on reaching capacity in put operation. also used in get operation, remove the node and add at tail (most recently used) 
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    def insert(self, node):     #insert at tail ; required for put or add at the end for get
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int: #add node to end
        if key in self.hm:   #deleting node and adding it to end
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])
        if len(self.hm) > self.cap:  # remove from the list and delete the least recently used from hashmap
            leastRecentlyUsed = self.head.next
            self.remove(leastRecentlyUsed)
            del self.hm[leastRecentlyUsed.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)