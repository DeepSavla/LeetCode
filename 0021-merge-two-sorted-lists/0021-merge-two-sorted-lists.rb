def merge_two_lists(list1, list2)
    prehead = ListNode.new(-1)

    prev = prehead

    while list1 && list2
        if list1.val<=list2.val
            prev.next = list1
            list1 = list1.next
        else
            prev.next = list2
            list2 = list2.next
        end
        prev = prev.next
    end
    prev.next = list1.nil?? list2:list1;
    prehead.next
end
