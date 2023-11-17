# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root.left,root.right)
        
    def isMirror(self,l,r):
        if l==None and r==None:
            return True
        if l== None or r==None:
            return False
        if l.val != r.val:
            return False
        if self.isMirror(l.left,r.right) and self.isMirror(l.right,r.left):
            return True