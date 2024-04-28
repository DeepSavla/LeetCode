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
        visitedHm = {}
        q = deque()
        if node == None:
            return node
        q.append(node)
        visitedHm[node.val] = Node(node.val,[])
        while len(q)!=0:
            s = q.popleft()
            for n in s.neighbors:
                if n.val not in visitedHm:
                    visitedHm[n.val] = Node(n.val,[])
                    q.append(n)
                visitedHm[s.val].neighbors.append(visitedHm[n.val])
        return visitedHm[node.val]
        
        