# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len = 0
        current=head
        while current != None:
            current = current.next
            len=len+1
        delEle = len-n
        current=head
        if len==1 and n==1:
            head = None
            return head
        if delEle ==0:
            head = head.next
        for i in range(1,delEle):
            current = current.next
        if current.next.next == None:
            current.next = None
        else:
            current.next = current.next.next
        return head
        
            
        
            