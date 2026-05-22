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
        # 初始化一个虚拟头节点，方便处理边界情况
        cur = ListNode(0)
        res = cur
        while list1 or list2:
            # 处理边界情况
            if not list1:
                cur.next = list2
                break
            elif not list2:
                cur.next = list1
                break
            # 处理一般情况
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return res.next

    def mergeTwoLists_(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 递归实现，不添加额外的空间
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_(list1, list2.next)
            return list2
