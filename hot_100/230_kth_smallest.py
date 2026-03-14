# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.kth = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = 0

        def inorder(root: Optional[TreeNode]) -> Optional[int]:
            if root is None:
                return None
            left = inorder(root.left)
            if left is not None:
                return left
            self.kth += 1
            if self.kth == k:
                return root.val
            right = inorder(root.right)
            if right is not None:
                return right
            # 易错点: 忘记返回None
            return None

        return inorder(root)


def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    if not level or level[0] is None:
        return None
    root = TreeNode(level[0])
    q = deque([root])
    i = 1
    while q and i < len(level):
        node = q.popleft()
        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            q.append(node.left)
        i += 1
        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            q.append(node.right)
        i += 1
    return root


# Test case: [5,3,6,2,4,null,null,1]
data = [5, 3, 6, 2, 4, None, None, 1]
root = build_tree(data)

solution = Solution()
print(solution.kthSmallest(root, 3))  # 3
