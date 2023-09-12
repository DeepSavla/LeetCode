# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root!=None:
            queue=[root]
            rtView = [root.val]
        else:
            return []
        while len(queue)>0:
            l=len(queue)
            for i in range(l):
                if queue[i].left !=None:
                    queue.append(queue[i].left)
                if queue[i].right !=None:
                    queue.append(queue[i].right)
            queue = queue[l::]
            if len(queue)>0:
                rtView.append(queue[-1].val)
        return rtView 
            
               
            
        