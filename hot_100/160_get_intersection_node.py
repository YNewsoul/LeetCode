# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针法
        # 单独指向对方的头节点，遍历到交点时，两个指针会同时到达交点
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

    def getIntersectionNode_(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 哈希表法
        # 遍历headA，将每个节点的地址存储到哈希表中
        # 遍历headB，如果headB中的节点地址在哈希表中，说明该节点是交点
        # 如果headB中的节点地址不在哈希表中，说明headB中没有交点
        hash_table = {}
        while headA:
            hash_table[headA] = headA
            headA = headA.next
        while headB:
            if headB in hash_table:
                return headB
            headB = headB.next
        return None
