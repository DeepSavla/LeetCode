# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        slow = head
        fast = head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                newPointer = head
                while newPointer !=slow:
                    newPointer = newPointer.next
                    slow = slow.next
                return slow
        return None
            
            
        