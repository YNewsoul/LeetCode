# 2. 两数相加

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum_list = ListNode()
        head = sum_list
        mark = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += mark
            mark = sum // 10
            sum_list.val = sum % 10
            if l1 or l2:
                new_node = ListNode()
                sum_list.next = new_node
                sum_list = new_node
            elif mark != 0:
                new_node = ListNode()
                new_node.val = mark
                sum_list.next = new_node
        return head


solution = Solution()
