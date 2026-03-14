# Definition for a binary tree node.
from typing import List, Optional

# 102. 二叉树的层序遍历
# 思路: 使用前序遍历, 记录当前节点的层数, 并将节点值添加到对应层的列表中


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.level_order = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def preorder(root: TreeNode, level: int):
            level += 1
            if root is None:
                return
            if level > len(self.level_order):
                self.level_order.append([])
            self.level_order[level - 1].append(root.val)
            preorder(root.left, level)
            preorder(root.right, level)

        preorder(root, 0)
        return self.level_order
