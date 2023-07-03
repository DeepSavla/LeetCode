# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def pre(node):
            if root == None:
                return
            res.append(node.val)
            if node.left != None:
                pre(node.left)
            if node.right != None:
                pre(node.right)
        pre(root)
        
        return res