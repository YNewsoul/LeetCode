# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代法
        # 从头节点开始，将每个节点的next指针指向它的前一个节点
        if not head:
            # 如果头节点为空，直接返回None
            return None
        # 初始化结果节点为头节点
        res = ListNode(head.val)
        while head.next:
            # 根据head.next.val创建新节点
            node = ListNode(head.next.val)
            # 将新节点插入到结果节点的头部
            node.next = res
            # 更新结果节点为新节点
            res = node
            # 更新head节点为head.next
            head = head.next
        return res
