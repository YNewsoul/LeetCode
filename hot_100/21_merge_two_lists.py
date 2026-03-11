# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = ListNode(0)
        res = cur
        while list1 or list2:
            if not list1:
                cur.next = list2
                break
            elif not list2:
                cur.next = list1
                break
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return res.next
