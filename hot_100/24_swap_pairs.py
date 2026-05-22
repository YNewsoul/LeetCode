# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

    # 采用递归的方式交换节点对
    def swapPairs_(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 交换当前节点对
        h1 = head
        h2 = head.next
        h1.next = h2.next
        h2.next = h1
        # 递归交换下一个节点对
        h1.next = self.swapPairs(h1.next)
        return h2
