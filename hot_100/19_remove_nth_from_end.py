# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 计算链表长度
        count = 0
        count_head = head
        while count_head:
            count += 1
            count_head = count_head.next
        index = 0
        res = head
        if count == n:
            return head.next
        # 遍历链表，找到要删除的节点的前一个节点
        while index < count - n - 1:
            index += 1
            head = head.next
        head.next = head.next.next
        return res

    # 2.使用栈来实现
    def removeNthFromEnd_(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        cur = head
        # 遍历链表，将每个节点入栈
        while cur:
            stack.append(cur)
            cur = cur.next
        # 从栈顶开始出栈，出栈n个节点
        for _ in range(n):
            stack.pop()

        # 如果栈为空，说明要删除的是头节点
        if not stack:
            return head.next
        pre = stack[-1]
        pre.next = pre.next.next
        return head

    # 3.快慢指针
    def removeNthFromEnd__(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast = head
        slow = head
        cout = 0
        while fast:
            fast = fast.next
            if cout > n:
                slow = slow.next
            cout += 1
        if cout == n:
            return head.next
        slow.next = slow.next.next
        return head
