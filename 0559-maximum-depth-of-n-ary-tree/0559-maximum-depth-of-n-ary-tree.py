"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        depth = 1
        for i in range(len(root.children)):
            curr = self.maxDepth(root.children[i]) + 1
            depth = max(depth,curr) 
        return depth
            