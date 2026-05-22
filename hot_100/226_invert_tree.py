# Definition for a binary tree node.
from typing import Optional


# 226. 翻转二叉树
# 思路：递归交换左右子树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归交换左右子树
        if root is None:
            return None
        # 交换左右子树就行了
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
