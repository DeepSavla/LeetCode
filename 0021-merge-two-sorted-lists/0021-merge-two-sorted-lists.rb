# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
    result = ListNode.new
    current = result
  
    while list1 && list2
        if list1.val < list2.val
            current.next = list1
            list1 = list1.next
        else
            current.next = list2
            list2 = list2.next
        end
        current = current.next
    end

    if list1 
        current.next = list1 
    else 
        current.next = list2
    end
    
    result.next
end