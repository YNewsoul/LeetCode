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
        # 递归检查左子树和右子树是否对称
        def check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                # 如果左右子树都为空，说明对称
                return True
            if left is None or right is None:
                # 如果左右子树只有一个为空，说明不对称
                return False
            if left.val != right.val:
                # 如果左右子树的根节点值不同，说明不对称
                return False
            # 递归检查左子树的右子树和右子树的左子树是否对称
            return check(left.left, right.right) and check(left.right, right.left)

        if root is None:
            return True
        # 递归检查左子树和右子树是否对称
        return check(root.left, root.right)
