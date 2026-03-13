# Definition for a binary tree node.
from typing import List, Optional


# 108. 将有序数组转换为二叉搜索树
# 思路：递归构建二叉搜索树，每次取数组中间元素作为根节点，左半部分作为左子树，右半部分作为右子树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid + 1 :])
            return root

        return build(nums)
