# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self):
        self.cout = 0
        self.max_deep = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 最大深度为1 + 左子树与右子树中较大的深度值
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_(self, root: Optional[TreeNode]) -> int:
        # 递归遍历
        # 左子树 -> 根节点 -> 右子树
        if root is None:
            return 0
        self.cout += 1
        self.maxDepth_(root.left)
        self.maxDepth_(root.right)
        self.max_deep = max(self.max_deep, self.cout)
        self.cout -= 1
        return self.max_deep
