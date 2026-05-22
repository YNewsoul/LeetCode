# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 数组法
    # 将链表转换为数组，判断数组是否为回文数组
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        return list == list[::-1]

    # 递归法
    def isPalindrome_(self, head: Optional[ListNode]) -> bool:
        # 使用全局变量，因为递归过程需要对此变量修改
        self.head_ = head

        def check(node: Optional[ListNode]):
            if node:
                # check 有可能返回 None，所以需要判断是否为 None
                if not check(node.next):
                    return False
                if node.val != self.head_.val:
                    return False
                self.head_ = self.head_.next
            return True

        return check(head)

    # 快慢指针法
    def isPalindrome__(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        # 找到链表的中间节点
        first_half_end = self.find_middle(head)
        # 反转后半部分链表
        second_half_start = self.reverse(first_half_end.next)

        # 检查是否为回文链表
        res = self.check(head, second_half_start)

        # 恢复链表
        first_half_end.next = self.reverse(second_half_start)
        return res

    def find_middle(self, head: Optional[ListNode]):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head: Optional[ListNode]):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def check(self, head_1: Optional[ListNode], head_2: Optional[ListNode]):
        while head_1 and head_2:
            if head_1.val != head_2.val:
                return False
            head_1 = head_1.next
            head_2 = head_2.next
        return True
