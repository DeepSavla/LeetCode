# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(node1):
            if node1 == None:
                return 0
            return max(getHeight(node1.left),getHeight(node1.right))+1
        
        if root==None:
            return True
        if abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        
            
        