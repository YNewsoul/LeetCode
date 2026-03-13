# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.cache = dict()

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        if head not in self.cache:
            new_node = Node(head.val)
            self.cache[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
        return self.cache[head]
