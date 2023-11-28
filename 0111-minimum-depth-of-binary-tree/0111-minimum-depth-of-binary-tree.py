# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root!= None and root.left == None and root.right == None:
            return 1
        if root!=None and root.left == None:
            rh= self.minDepth(root.right)
            lh = 10000
        elif root!=None and root.right == None:
            lh= self.minDepth(root.left)
            rh = 10000
        else:
            lh= self.minDepth(root.left)
            rh= self.minDepth(root.right)
        return min(lh,rh)+1