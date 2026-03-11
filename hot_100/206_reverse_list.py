# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = ListNode(head.val)
        while head.next:
            node = ListNode(head.next.val)
            node.next = res
            res = node
            head = head.next
        return res
