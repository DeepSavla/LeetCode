# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=[[root,0]]
        levOr =[]
        while len(queue)>0:
            if root == None:
                return []
            if len(levOr)<=queue[0][1]:
                levOr.insert(queue[0][1],[queue[0][0].val])
            else:
                levOr[queue[0][1]].append(queue[0][0].val)
            if queue[0][0].left!=None:
                queue.append([queue[0][0].left,queue[0][1]+1])
            if queue[0][0].right!=None:
                queue.append([queue[0][0].right,queue[0][1]+1])
            queue.pop(0)
        return levOr