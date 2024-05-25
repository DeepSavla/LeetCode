# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        s = set()
        curr = head
        while curr!=None:
            setSize = len(s)
            s.add(curr)
            if setSize == len(s):
                return curr
            curr = curr.next
        return None
            
            
        