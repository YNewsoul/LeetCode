# Definition for a binary tree node.
from typing import List, Optional

# 199. 二叉树的右视图
# 思路:使用右序遍历,用哈希记录每个level的第一个节点，这个节点就是右边先看到的


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hash_res = {}

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            dfs(node.right, level + 1)
            if level not in self.hash_res:
                self.hash_res[level] = node.val
            dfs(node.left, level + 1)

        dfs(root, 0)
        return [self.hash_res[i] for i in range(len(self.hash_res))]


solution = Solution()

# Tree: [1,2,3,null,5,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(4)

print(solution.rightSideView(root))  # [1, 3, 4]
