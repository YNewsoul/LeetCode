from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# 构建树
# 树的结构
#       A
#     /   \
#    B     C
#   / \
#  D   E
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

# 前序遍历
print(preorder(root))  # ['A', 'B', 'D', 'E', 'C']

# 中序遍历
print(inorder(root))  # ['D', 'B', 'E', 'A', 'C']

# 后序遍历
print(postorder(root))  # ['D', 'E', 'B', 'C', 'A']
