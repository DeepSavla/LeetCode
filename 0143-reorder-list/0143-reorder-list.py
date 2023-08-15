# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if head == None:
            return head
        
        """getting second half in sp"""
        sp = head
        fp=head
        while fp!=None and fp.next!=None:
            fp = fp.next.next
            sp=sp.next
        
        """reversing second half(mid onwards)"""
        prev=None
        curr=sp.next
        while curr!=None:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        head2 = prev
        
        """Merging head and head1 (i.e. first half and reversed second half)"""
        head1=head
        sp.next=None
        while head2!=None:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
        
        
            
            
        