# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists)>1:
            curMergedLists =[]
            for i in range(0,len(lists),2):
                list1 = lists[i]
                if i+1<len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                curMergedLists.append(self.mergeTwoLists(list1,list2))
            lists = curMergedLists
        return lists[0]
            
    
    
    def mergeTwoLists(self,l1,l2):
        head = ListNode(-1)
        current=head
        while l1 or l2:
            if l1==None:
                current.next = ListNode(l2.val)
                l2=l2.next
            elif l2==None:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val<l2.val:
                    current.next = ListNode(l1.val)
                    l1=l1.next
                else:
                    current.next = ListNode(l2.val)
                    l2=l2.next   
            current = current.next
        return head.next
        
        
       
        