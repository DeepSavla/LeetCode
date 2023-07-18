# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        previous = head
        current = previous.next
        previous.next = None
        while current !=None:
            next = current.next
            if next == None:
                head=current
            current.next = previous
            previous=current
            current=next
        return head
        