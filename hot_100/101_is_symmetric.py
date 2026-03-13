# Definition for a binary tree node.

from typing import Optional

# 101. 对称二叉树
# 思路：递归检查左子树和右子树是否对称
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)

        if root is None:
            return True
        return check(root.left, root.right)
