# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if node == None:
                return 0
            lh = getHeight(node.left)
            rh = getHeight(node.right)
            return max(lh,rh)+1
    
        if root==None:
            return True
        if abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        