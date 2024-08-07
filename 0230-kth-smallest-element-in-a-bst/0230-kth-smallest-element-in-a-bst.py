# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array =[]
        def inorder(root):
            nonlocal array
            if root==None:
                return
            if root.left:
                inorder(root.left)
            array.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return array[k-1]
            