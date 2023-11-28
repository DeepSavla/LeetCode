# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0
#         if root.left == None and root.right == None:
#             return 1
#         elif root.left == None:
#             rh= self.minDepth(root.right)
#             lh = math.inf
#         elif root.right == None:
#             lh= self.minDepth(root.left)
#             rh = math.inf
#         else:
#             lh= self.minDepth(root.left)
#             rh= self.minDepth(root.right)
#         return min(lh,rh)+1


#approach 2
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None:
            return self.minDepth(root.right)+1
        elif root.right == None:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        