# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathTotal(root, sum):
            if root==None:
                return
            sum = sum+root.val 
            if sum == targetSum and root.left == None and root.right==None:
                return True
            return pathTotal(root.left,sum) or pathTotal(root.right,sum)
            
        
        return pathTotal(root, 0)