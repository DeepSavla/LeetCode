# FileName: p2
# Author: Lebin Zhou
# CreatTime: 2023-10-09 21:23
# Description: 
# Version: 1.0

# frozen_string_literal: true

# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}

def merge_two_lists(list1, list2)
  result = ListNode.new(-1, nil)

  dummy = result
  p1, p2 = list1, list2

  while p1 != nil and p2 != nil do
    if p1.val < p2.val
      dummy.next = ListNode.new(p1.val, nil)
      p1 = p1.next
    else
      dummy.next = ListNode.new(p2.val, nil)
      p2 = p2.next
    end
    dummy = dummy.next
  end

  if p1 != nil
    dummy.next = p1
  end

  if p2 != nil
    dummy.next = p2
  end

  return result.next
end