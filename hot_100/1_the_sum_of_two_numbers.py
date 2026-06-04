# 1.两数之和

from typing import List

"思路：哈希表"


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用 哈希表 存储已经遍历过的数字和它的索引，时间复杂度O(n)，空间复杂度O(n)
        num_dict = {}
        for i, num in enumerate(nums):
            # 遍历数组，如果目标值减去当前数字在哈希表中，说明找到了两个数，返回它们的索引
            if target - num in num_dict:
                return [num_dict[target - num], i]
            # 如果不在哈希表中，说明当前数字还没有被遍历过，将当前数字和它的索引添加到哈希表中
            num_dict[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
