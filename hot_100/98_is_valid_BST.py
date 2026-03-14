# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(node: TreeNode, lower=float("-inf"), upper=float("inf")) -> bool:
            if node is None:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 错误点: 递归时, 左子树的上界应该是当前节点的值,下界不变, 右子树的下界应该是当前节点的值,上界不变
            return preorder(node.left, lower, val) and preorder(node.right, val, upper)

        return preorder(root, float("-inf"), float("inf"))
