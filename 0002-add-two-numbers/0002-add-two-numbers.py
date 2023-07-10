# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1=l1
        cur2=l2
        carryFlag=False
        node1 = None
        while cur1!=None or cur2 != None or carryFlag:
            val1 = 0
            val2 = 0
            if cur1!=None:
                val1 = cur1.val
                cur1 = cur1.next
            if cur2!=None:
                val2 = cur2.val
                cur2=cur2.next
            add = val1 + val2
            if carryFlag:
                add = add+1
            if add>9:
                add = add-10
                carryFlag= True
            else:
                carryFlag= False
            if node1:
                node1.next = ListNode(add)
                node1 = node1.next
            else:
                node1 = ListNode(add)
                head = node1
        return head
            