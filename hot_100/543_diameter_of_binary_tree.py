# Definition for a binary tree node.
from typing import Optional


# 543. 二叉树的直径
# 思路：递归计算每个节点的高度，直径为左子树高度 + 右子树高度
# 维护一个全局变量res，用于记录直径
# 直径可能在左子树、右子树、根节点中
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node: Optional[TreeNode]):
            if node is None:
                return 0
            l = height(node.left)
            r = height(node.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)

        height(root)
        return self.res
