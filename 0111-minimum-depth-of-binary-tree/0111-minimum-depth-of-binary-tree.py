# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root!= None and root.left == None and root.right == None:
            return 1
        if root!=None and root.left == None:
            rh= self.minDepth(root.right)
            lh = math.inf
        elif root!=None and root.right == None:
            lh= self.minDepth(root.left)
            rh = math.inf
        else:
            lh= self.minDepth(root.left)
            rh= self.minDepth(root.right)
        return min(lh,rh)+1