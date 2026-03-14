# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 先序遍历,将节点顺序记录下来
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    # 错误解法，这种情况由于递归关系，会导致回溯的时候丢失掉已指向的信息
    def flatten_(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root, node: Optional[TreeNode]):
            if node is None:
                return
            right = node.right
            left = node.left

            root.right = node
            root.left = None
            preorder(node, left)
            preorder(node, right)

        new_root = TreeNode()
        preorder(new_root, root)
        root = new_root.right


soluton = Solution()

# Input tree: [1,2,5,3,4,null,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

solution = Solution()
solution.flatten(root)
