# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #finding length of ll
        if head ==None:
            return head
        p1 = head
        lenLL = 1
        while p1.next != None:
            p1 = p1.next
            lenLL += 1
        #now p1 is at last node
        # so we make first node at next
        p1.next = head
        #if k is greater than len of LL
        k = k % lenLL
        #now break the LL and set new head
        breakPoint = lenLL - k -1
        p2=head
        for i in range(breakPoint):
            p2=p2.next
        head = p2.next
        p2.next = None
        return head