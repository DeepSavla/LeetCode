# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(node):
            if root == None:
                return
            if node.left != None:
                inorder(node.left)
            res.append(node.val)
            if node.right != None:
                inorder(node.right)
        inorder(root)
        return res