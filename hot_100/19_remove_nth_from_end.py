# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        count_head = head
        while count_head:
            count += 1
            count_head = count_head.next
        index = 0
        res = head
        if count == n:
            return head.next
        while index < count - n - 1:
            index += 1
            head = head.next
        head.next = head.next.next
        return res
