# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 哈希表法，把过程中的节点都加入哈希表，如果重复加入，说明有环，返回重复加入的节点
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while head:
            if head in list:
                return head
            list.append(head)
            head = head.next
        return None

    # 快慢指针法，如果快指针追上慢指针，说明有环
    def detectCycle_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # 返回快慢指针相遇节点
        def get_intersection_node(head: Optional[ListNode]) -> Optional[ListNode]:
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast
            return None

        intersection_node = get_intersection_node(head)
        if intersection_node is None:
            return None

        # 找到环的入口节点,有数学公式证明的
        slow = head
        while slow != intersection_node:
            slow = slow.next
            intersection_node = intersection_node.next
        return slow
