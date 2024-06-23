# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def maxNodePath(root,maxVal):
            nonlocal goodNodes
            if root==None:
                return
            if root.val>=maxVal:
                goodNodes +=1
            maxNodePath(root.left, max(root.val, maxVal))
            maxNodePath(root.right, max(root.val, maxVal))
            
        maxNodePath(root, -math.inf)
        return goodNodes
        