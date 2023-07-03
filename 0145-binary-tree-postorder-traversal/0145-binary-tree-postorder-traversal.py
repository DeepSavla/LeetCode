# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def post(node):
            if root == None:
                return
            if node.left != None:
                post(node.left)
            if node.right != None:
                post(node.right)
            res.append(node.val)
        post(root)
        return res