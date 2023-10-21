"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue=[[root,0]]
        levOr =[]
        while len(queue)>0:
            if root == None:
                return root
            if len(levOr)<=queue[0][1]:
                levOr.insert(queue[0][1],[queue[0][0]])
            else:
                levOr[queue[0][1]].append(queue[0][0])
            if queue[0][0].left!=None:
                queue.append([queue[0][0].left,queue[0][1]+1])
            if queue[0][0].right!=None:
                queue.append([queue[0][0].right,queue[0][1]+1])
            queue.pop(0)
        for i in range(len(levOr)):
            for j in range(len(levOr[i])):
                if  j !=len(levOr[i]) -1:
                    levOr[i][j].next = levOr[i][j+1]
        return root