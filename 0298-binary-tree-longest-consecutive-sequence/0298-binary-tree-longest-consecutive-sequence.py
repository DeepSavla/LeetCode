# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.findLongest(root, root.left, 1), self.findLongest(root, root.right, 1))
            
        
    def findLongest(self, parent, cur, curSeq):
        if cur == None:
            return curSeq
        if cur.val == parent.val + 1:
            curSeq= curSeq + 1
        else:
            curSeq = 1
        curSeq = max(curSeq, self.findLongest(cur, cur.left,curSeq), self.findLongest(cur, cur.right,curSeq))
        return curSeq
                