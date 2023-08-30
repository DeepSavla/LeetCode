# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameTree(p,q):
            if p==None and q==None:
                return True
            if (p==None and q!=None) or (p!=None and q==None):
                return False
            if p.val!=q.val:
                return False
            if isSameTree(p.left,q.left) and isSameTree(p.right,q.right):
                return True
            return False
        
        if root==None:
            return False
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
            
        
        
            