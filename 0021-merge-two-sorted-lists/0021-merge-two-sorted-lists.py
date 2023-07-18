# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=None
        while list1!=None or list2!=None:
            if list1== None:
                node = ListNode(list2.val)
                list2=list2.next
            elif list2==None:
                node = ListNode(list1.val)
                list1=list1.next
            else:
                if list1.val<list2.val:
                    node = ListNode(list1.val)
                    list1=list1.next
                else:
                    node = ListNode(list2.val)
                    list2=list2.next
            if head==None:
                head=node
                temp=node
            else:
                temp.next=node
                temp=temp.next
        return head
        