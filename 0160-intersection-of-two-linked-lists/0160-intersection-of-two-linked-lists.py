# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 1
        lenB = 1
        ptrA = headA
        ptrB = headB
        while ptrA!=None:
            lenA+=1
            ptrA = ptrA.next
        while ptrB!=None:
            lenB+=1
            ptrB = ptrB.next
        ptrA = headA
        ptrB = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                ptrA = ptrA.next
        elif lenB>lenA:
            for i in range(lenB - lenA):
                ptrB = ptrB.next
        while ptrA !=None:
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        return None
        