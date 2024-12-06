"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        print(node)
        if node == None:
            return None
        q = deque()
        hm = {}
        q.append(node)
        hm[node] = Node(node.val)
        while q:
            oldNode = q.popleft()
            for n in oldNode.neighbors:
                if n not in hm.keys():
                    hm[n] = Node(n.val)
                    q.append(n)
                hm[oldNode].neighbors.append(hm[n])
        return hm[node]
            
        

        