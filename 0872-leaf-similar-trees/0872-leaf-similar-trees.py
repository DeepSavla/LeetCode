# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr = []
        def leafNodes(node):
            if node.left==None and node.right==None:
                arr.append(node.val)
                return
            if node.left!=None:
                leafNodes(node.left)
            if node.right!=None:
                leafNodes(node.right)
        
         
        leafNodes(root1)
        arr1 = arr
        arr=[]
        leafNodes(root2)
        if arr1 == arr:
            return True
        else:
            return False