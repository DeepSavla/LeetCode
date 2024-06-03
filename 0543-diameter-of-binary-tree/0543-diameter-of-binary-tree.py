# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we know that longest path always has leaf nodes
        #Hence for every node, we calculate the longest left and the longest right path and calculate the current max path
        d = 0
        def maxHeight(node):
            nonlocal d
            if node ==None:
                return 0
            left = maxHeight(node.left)
            right = maxHeight(node.right) 
            d = max(d , left+right)
            print(d)
            return max(left,right)+1
        
        maxHeight(root)
        return d
        
        
        