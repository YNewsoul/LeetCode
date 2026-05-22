# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 哈希表法，把过程中的节点都加入哈希表，如果重复加入，说明有环
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    # 快慢指针法，如果快指针追上慢指针，说明有环
    def hasCycle_(self, head: ListNode) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
