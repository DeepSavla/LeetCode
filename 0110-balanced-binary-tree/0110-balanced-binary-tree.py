# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getHeight(self, node1):
        if node1 == None:
            return 0
        return max(self.getHeight(node1.left),self.getHeight(node1.right))+1
    
    def isBalanced(self, root):
        if root==None:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        
            
        