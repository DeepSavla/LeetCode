# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slowP=head
        fastP=head
        while fastP !=None and fastP.next!=None:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP==fastP:
                return True
        return False
        